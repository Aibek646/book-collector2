from django.contrib import admin
from .models import Book, Print, Translator
# Register your models here.
admin.site.register(Book)
admin.site.register(Print)
admin.site.register(Translator)

