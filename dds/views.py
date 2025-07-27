from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django_filters.views import FilterView
from .models import Record, SubCategory
from .forms import RecordForm
from .filters import RecordFilter

class RecordListView(ListView):
    model = Record
    template_name = 'record_list.html'
    context_object_name = 'records'

class RecordCreateView(CreateView):
    model = Record
    form_class = RecordForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('record_list')

class RecordUpdateView(UpdateView):
    model = Record
    form_class = RecordForm
    template_name = 'record_form.html'
    success_url = reverse_lazy('record_list')

class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'record_confirm_delete.html'
    success_url = reverse_lazy('record_list')

class RecordListView(FilterView):
    model = Record
    template_name = 'record_list.html'
    context_object_name = 'records'
    filterset_class = RecordFilter

def load_subcategories(request):
    category_id = request.GET.get('category_id')
    if category_id:
        subcategories = SubCategory.objects.filter(category_id=category_id).values('id', 'name')
    else:
        subcategories = []
    return JsonResponse(list(subcategories), safe=False)
