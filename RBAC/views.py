from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django.contrib.auth.models import User, Group, Permission
from RBAC.serializers import UserSerializer, GroupSerializer, PermissionSerializer
from rest_framework import permissions

class UserViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a user instance.

        list:
            Return all users, ordered by most recently joined.

        create:
            Create a new user.

        delete:
            Remove an existing user.

        partial_update:
            Update one or more fields on an existing user.

        update:
            Update a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
            retrieve:
                Return a user instance.

            list:
                Return all users, ordered by most recently joined.

            create:
                Create a new user.

            delete:
                Remove an existing user.

            partial_update:
                Update one or more fields on an existing user.

            update:
                Update a user.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class PermissionViewSet(viewsets.ModelViewSet):
    """
            retrieve:
                Return a user instance.

            list:
                Return all users, ordered by most recently joined.

            create:
                Create a new user.

            delete:
                Remove an existing user.

            partial_update:
                Update one or more fields on an existing user.

            update:
                Update a user.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)