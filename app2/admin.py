from django.contrib import admin
from .models import Number
# Register your models here.

class ModalAdmin(admin.ModelAdmin):
    list_display = ('username', 'number')


admin.site.register(Number, ModalAdmin)