from rest_framework import serializers
from CheckIn.models import CheckIn

class CheckInSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model = CheckIn
        fields = ('url','appId', 'userId', 'date')
        extra_kwargs = {'appId':{'help_text':'{integer} which represents an app.'},
                        'userId':{'help_text':'{sting} which represents the userid or username.'},
                        'datetime':{'help_text':'{string} [YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z] which represents '
                                            'the checkin date. Defaut is now.',
                                'required': False}
                        }
