# Create your views here.
from rest_framework import viewsets
from CheckIn.models import CheckIn
from CheckIn.serializers import CheckInSerializer
import CheckIn.permissions as CPermissions

# Create your views here.
class CheckInViewSet(viewsets.ModelViewSet):
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
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer
    permission_classes = (CPermissions.CheckInPostOnly,)

