from django.contrib import admin
from .models import Candidate

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email','gender','career']
    search_fields = ['name','phone','email']
    list_filter = ['gender','career']
    list_per_page = 10
    
    admin.site.register(Candidate,)
    