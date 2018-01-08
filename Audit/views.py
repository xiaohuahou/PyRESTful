from rest_framework import viewsets
from Audit.models import Book
from Audit.serializers import BookSerializer
from rest_framework import permissions

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
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
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.DjangoModelPermissions,)