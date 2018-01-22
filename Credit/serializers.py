from rest_framework import serializers
from Credit.models import Credit
from Credit.models import CreditLog

class CreditLogSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="creditlog_v1:creditlog-detail")

    class Meta:
        model = CreditLog
        fields = ('url', 'id', 'appId', 'userId', 'credit', 'datetime')
        extra_kwargs = {'appId':{'help_text':'{integer} which represents an app.'},
                        'userId':{'help_text':'{sting} which represents the userid or username.'},
                        'credit':{'help_text':'{integer} which represents the credit. '
                                                'Eg: 0, 1, -1 '
                                                'Defaut is 0.',
                                'required': False},
                        'datetime': {'help_text': '{string} [YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z] '
                                                  'which represents the checkin date. '
                                                  'Eg: "2018-01-12T15:27:01.700348+08:00" '
                                                  'Defaut is now.',
                                'required': False}
                        }

class CreditSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="credit_v1:credit-detail")

    class Meta:
        model = Credit
        fields = ('url', 'id', 'appId', 'userId', 'credit')
        extra_kwargs = {'appId':{'help_text':'{integer} which represents an app.'},
                        'userId':{'help_text':'{sting} which represents the userid or username.'},
                        'credit':{'help_text':'{integer} which represents the credit. '
                                                'Eg: 0, 1, -1 '
                                                'Defaut is 0.',
                                'required': False}
                        }