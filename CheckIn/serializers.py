from rest_framework import serializers
from CheckIn.models import CheckIn

class CheckInSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = CheckIn
        fields = ('url','appId', 'userId', 'date')
