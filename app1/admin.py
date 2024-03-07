from django.contrib import admin
from .models import MorakhsiDetailView,PersonalInfromation,PersonelPresenceAbsence,Number
# Register your models here.

admin.site.register(MorakhsiDetailView)
admin.site.register(PersonalInfromation)
admin.site.register(PersonelPresenceAbsence)

class ModalAdmin(admin.ModelAdmin):
    list_display = ('username', 'number')


admin.site.register(Number, ModalAdmin)



    
