import django_filters
from django_filters import DateTimeFromToRangeFilter, ChoiceFilter

from .models import Tasks, Purposes


class TasksFilter(django_filters.FilterSet):
    deadline = DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    date_complete = DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Tasks
        fields = [
            'deadline',
            'date_complete',
        ]


class PurposesFilter(django_filters.FilterSet):
    deadline = DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))
    date_complete = DateTimeFromToRangeFilter(widget=django_filters.widgets.RangeWidget(attrs={'type': 'date'}))

    class Meta:
        model = Purposes
        fields = [
            'deadline',
            'date_complete',
        ]
