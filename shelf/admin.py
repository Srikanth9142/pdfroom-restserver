from django.contrib import admin
from .models import Book,Analytic,Reader,ShelfBook, Comment
# Register your models here.
admin.site.register(Book)
admin.site.register(Analytic)
admin.site.register(Reader)
admin.site.register(ShelfBook)
admin.site.register(Comment)
