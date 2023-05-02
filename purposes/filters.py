import django_filters
from django_filters import DateTimeFromToRangeFilter

from .models import Purposes


class PurposesFilter(django_filters.FilterSet):
    deadline = DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    date_complete = DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Purposes
        fields = [
            'deadline',
            'date_complete',
        ]
