from django.contrib import admin
from .models import Status, Type, Category, SubCategory, Record

admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Record)
