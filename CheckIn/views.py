import datetime
from dateutil import parser
# Create your views here.
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from CheckIn.models import CheckIn
from CheckIn.serializers import CheckInSerializer
from CheckIn.schemas import CheckInSchema
from CheckIn.filtersets import CheckInFilterSet
import CheckIn.permissions as CPermissions

from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#Filter
class CheckInDjangoFilterBackend(DjangoFilterBackend):
    default_filter_set = CheckInFilterSet

class CheckInViewSet(viewsets.ModelViewSet):
    """
            retrieve:
                Return a CheckIn instance.

            list:
                Return all CheckIn, ordered by most recently joined.

            create:
                Create a new CheckIn.

            delete:
                Remove an existing CheckIn.

            partial_update:
                Update one or more fields on an existing user.

            update:
                Update a CheckIn.
    """
    queryset = CheckIn.objects.all()
    serializer_class = CheckInSerializer

    permission_classes = (CPermissions.CheckInPostOnly,)

    filter_backends = (CheckInDjangoFilterBackend,)
    filter_fields = ('appId', 'userId')

    schema = CheckInSchema()

    def create(self, request, *args, **kwargs):
        request.data['datetime'] = datetime.datetime.now() if 'datetime' not in request.data else parser.parse(request.data['datetime'])
        return super(CheckInViewSet,self).create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        #over_ride the delete
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


