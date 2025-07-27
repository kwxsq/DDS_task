from django.urls import path
from .views import (
    RecordListView, RecordCreateView, RecordUpdateView, RecordDeleteView,
    load_subcategories
)

urlpatterns = [
    path('', RecordListView.as_view(), name='record_list'),
    path('add/', RecordCreateView.as_view(), name='record_add'),
    path('edit/<int:pk>/', RecordUpdateView.as_view(), name='record_edit'),
    path('delete/<int:pk>/', RecordDeleteView.as_view(), name='record_delete'),
    path('ajax/load-subcategories/', load_subcategories, name='ajax_load_subcategories'),
]
