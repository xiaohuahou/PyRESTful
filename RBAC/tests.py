from django.db import models
from django.test import TestCase
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from django.test.utils import isolate_apps
from django.test import Client
# Create your tests here.
# This test only test the underlying models

# This model automatically receives app_label='RBAC'
@isolate_apps('RBAC')
class UserGroupPermissionTests(TestCase):

    @classmethod
    def setUpClass(cls):

        class TestModel(models.Model):

            title = models.TextField()
            content = models.TextField()

            class Meta:
                permissions = (
            ("open_discussion", "Can create a discussion"),
            ("reply_discussion", "Can reply discussion"),
            ("close_discussion", "Can remove a discussion by setting its status as closed"),
        )

            def __str__(self):
                return self.title
        # create permissions group
        content_type = ContentType.objects.get_for_model(TestModel)

        Permission(name="Can create a discussion", codename='open_discussion', content_type=content_type).save()
        Permission(name="Can reply discussion", codename='reply_discussion', content_type=content_type).save()
        Permission(name="Can remove a discussion by setting its status as closed", codename='close_discussion', content_type=content_type).save()

        cls.openPermission = Permission.objects.get(codename='open_discussion', content_type=content_type,)
        cls.replyPermission = Permission.objects.get(codename='reply_discussion', content_type=content_type,)
        cls.closePermission = Permission.objects.get(codename='close_discussion', content_type=content_type,)

        cls.adminGroup = Group(name="AdminGroup")
        cls.adminGroup.save()
        cls.editorGroup = Group(name="EditorGroup")
        cls.editorGroup.save()
        cls.readerGroup = Group(name="ReaderGroup")
        cls.readerGroup.save()

        cls.admin = User.objects.create_user(username="admin", email="test@test.com", password="test", is_superuser=True)
        cls.editor = User.objects.create_user(username="editor", email="test@test.com", password="test", is_staff=True)
        cls.reader = User.objects.create_user(username="reader", email="test@test.com", password="test", is_staff=True)

        super(UserGroupPermissionTests, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.adminGroup.delete()
        cls.editorGroup.delete()
        cls.readerGroup.delete()

        cls.admin.delete()
        cls.editor.delete()
        cls.reader.delete()

        cls.openPermission.delete()
        cls.replyPermission.delete()
        cls.closePermission.delete()

    def test_run_sequentially(self):
        self.__UserPerm()
        self.__GroupPerm()

    def __check_after_setting(self):
        self.admin = User.objects.get(username="admin")
        self.assertTrue(self.admin.has_perm('RBAC.open_discussion'))
        self.assertTrue(self.admin.has_perm('RBAC.reply_discussion'))
        self.assertTrue(self.admin.has_perm('RBAC.close_discussion'))
        #
        self.editor = User.objects.get(username="editor")
        self.assertTrue(self.editor.has_perm('RBAC.open_discussion'))
        self.assertTrue(self.editor.has_perm('RBAC.reply_discussion'))
        self.assertFalse(self.editor.has_perm('RBAC.close_discussion'))
        #
        self.reader = User.objects.get(username="reader")
        self.assertFalse(self.reader.has_perm('RBAC.open_discussion'))
        self.assertFalse(self.reader.has_perm('RBAC.reply_discussion'))
        self.assertTrue(self.reader.has_perm('RBAC.close_discussion'))

    def __check_after_clear(self):
        # clear
        self.admin.user_permissions.clear()
        self.editor.user_permissions.clear()
        self.reader.user_permissions.clear()

        # admin is super, assertTrue even clear
        self.admin = User.objects.get(username="admin")
        self.assertTrue(self.admin.has_perm('RBAC.open_discussion'))
        self.assertTrue(self.admin.has_perm('RBAC.reply_discussion'))
        self.assertTrue(self.admin.has_perm('RBAC.close_discussion'))
        #
        self.editor = User.objects.get(username="editor")
        self.assertFalse(self.editor.has_perm('RBAC.open_discussion'))
        self.assertFalse(self.editor.has_perm('RBAC.reply_discussion'))
        self.assertFalse(self.editor.has_perm('RBAC.close_discussion'))
        #
        self.reader = User.objects.get(username="reader")
        self.assertFalse(self.reader.has_perm('RBAC.open_discussion'))
        self.assertFalse(self.reader.has_perm('RBAC.reply_discussion'))
        self.assertFalse(self.reader.has_perm('RBAC.close_discussion'))

    def __UserPerm(self):
        self.admin.user_permissions.add(self.openPermission, self.replyPermission, self.closePermission)
        self.editor.user_permissions.add(self.openPermission, self.replyPermission)
        self.reader.user_permissions.add(self.closePermission)

        self.__check_after_setting()

        #we need to reload the model
        self.__check_after_clear()

    def __GroupPerm(self):
        #make sure users has no permission except admin
        self.__check_after_clear()
        #

        self.adminGroup.permissions.add(self.openPermission, self.replyPermission, self.closePermission)
        self.editorGroup.permissions.add(self.openPermission, self.replyPermission)
        self.readerGroup.permissions.add(self.closePermission)
        #

        #add user
        self.adminGroup.user_set.add(self.admin)
        self.editorGroup.user_set.add(self.editor)
        self.readerGroup.user_set.add(self.reader)

        #check again
        self.__check_after_setting()
