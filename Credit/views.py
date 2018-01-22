# Create your views here.
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from Credit.models import Credit
from Credit.serializers import CreditSerializer
from Credit.schemas import CreditSchema
from Credit.filtersets import CreditFilterSet
import Credit.permissions as CPermissions

from rest_framework.response import Response
from rest_framework import status

# Create your views here.
#Filter
class CreditDjangoFilterBackend(DjangoFilterBackend):
    default_filter_set = CreditFilterSet

class CreditViewSet(viewsets.ModelViewSet):
    """
            retrieve:
                Return a Credit instance.

            list:
                Return all Credit, ordered by most recently joined.

            create:
                Create a new Credit.

            delete:
                Remove an existing Credit.

            partial_update:
                Update one or more fields on an existing user.

            update:
                Update a Credit.
    """
    queryset = Credit.objects.all()
    serializer_class = CreditSerializer

    permission_classes = (CPermissions.CreditPostOnly,)

    filter_backends = (CreditDjangoFilterBackend,)
    filter_fields = ('appId', 'userId')

    schema = CreditSchema()

    def create(self, request, *args, **kwargs):
        request.data['credit'] = request.data.get('credit', 0)
        return super(CreditViewSet,self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.data['credit'] = request.data.get('credit', 0)
        return super(CreditViewSet, self).update(request, *args, **kwargs)
    #
    def destroy(self, request, *args, **kwargs):
        #over_ride the delete
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        self.perform_destroy(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


#CreditLog Viewset here.
from Credit.models import CreditLog
from Credit.serializers import CreditLogSerializer

class CreditLogViewSet(viewsets.ModelViewSet):
    """
            retrieve:
                Return a CreditLog instance.

            list:
                Return all CreditLog, ordered by most recently joined.

            create:
                Create a new CreditLog.

            delete:
                Remove an existing CreditLog.

            partial_update:
                Update one or more fields on an existing user.

            update:
                Update a CreditLog.
    """
    queryset = CreditLog.objects.all()
    serializer_class = CreditLogSerializer

    permission_classes = (CPermissions.CreditPostOnly,)

    filter_backends = (CreditDjangoFilterBackend,)
    filter_fields = ('appId', 'userId')

    schema = CreditSchema()

    # def create(self, request, *args, **kwargs):
    #     request.data['credit'] = request.data.get('credit', 0)
    #     return super(CreditLogViewSet,self).create(request, *args, **kwargs)
    #
    # def update(self, request, *args, **kwargs):
    #     request.data['credit'] = request.data.get('credit', 0)
    #     return super(CreditLogViewSet, self).update(request, *args, **kwargs)
    # #
    # def destroy(self, request, *args, **kwargs):
    #     #over_ride the delete
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     self.perform_destroy(instance)
    #     return Response(serializer.data, status=status.HTTP_200_OK)