from django.db import models
from Credit.models import Credit
from django_filters import utils, filters
from django_filters.rest_framework import FilterSet

CHECKIN_FILTER_EXTRAS = {
    utils.get_model_field(Credit, 'appId'): {'help_text': '{integer} which represents an app.'},
    utils.get_model_field(Credit, 'userId'): {'help_text': '{sting} which represents the userid or username.'}
}

class CreditFilterSet(FilterSet):

    class Meta:
        filter_overrides = {
            models.PositiveIntegerField : {'filter_class': filters.NumberFilter,
                                            'extra': lambda field : CHECKIN_FILTER_EXTRAS.get(field,{})},
            models.CharField : {'filter_class': filters.CharFilter,
                                            'extra': lambda field : CHECKIN_FILTER_EXTRAS.get(field,{})},
        }
