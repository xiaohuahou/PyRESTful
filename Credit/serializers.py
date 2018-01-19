from rest_framework import serializers
from Credit.models import Credit

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