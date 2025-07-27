import django_filters
from .models import Record, Category, SubCategory, Status, Type
from django import forms

class RecordFilter(django_filters.FilterSet):
    date__gte = django_filters.DateFilter(field_name='date', lookup_expr='gte', label='Дата от', widget=forms.DateInput(attrs={'type': 'date'}))
    date__lte = django_filters.DateFilter(field_name='date', lookup_expr='lte', label='Дата до', widget=forms.DateInput(attrs={'type': 'date'}))
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())
    type = django_filters.ModelChoiceFilter(queryset=Type.objects.all())
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    subcategory = django_filters.ModelChoiceFilter(queryset=SubCategory.objects.all())

    class Meta:
        model = Record
        fields = ['date__gte', 'date__lte', 'status', 'type', 'category', 'subcategory']
