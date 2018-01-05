from rest_framework import serializers
from django.contrib.auth.models import User, Group, Permission

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'password')


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'id', 'name')


class PermissionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Permission
        fields = ('url', 'id', 'content_type_id','codename', 'name')