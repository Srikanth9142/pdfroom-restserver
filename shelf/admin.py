from django.contrib import admin
from .models import Book,Analytic,Reader
# Register your models here.
admin.site.register(Book)
admin.site.register(Analytic)
admin.site.register(Reader)
