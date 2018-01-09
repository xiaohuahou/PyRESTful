from rest_framework import viewsets
from Audit.models import Book, Auditing
from Audit.serializers import BookSerializer, AuditingSerializer
from rest_framework import permissions
import Audit.permissions as Apermissions

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

    def perform_create(self, serializer):
        # I am not sure this is the correct place to create the associate Auditing object.
        # Place the logic here for now.
        o = Auditing.objects.create()
        assert isinstance(o, Auditing)
        # you need to pass in the extra relation fields
        serializer.save(auditing_id=o.id)


class AuditingViewSet(viewsets.ModelViewSet):
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
    queryset = Auditing.objects.all()
    serializer_class = AuditingSerializer
    permission_classes = (permissions.DjangoModelPermissions,)