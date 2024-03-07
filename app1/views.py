from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import MorakhsiDetailView,PersonalInfromation,PersonelPresenceAbsence
import requests

# Create your views here.




def morakhasi(request):
    num = request.GET.get('num')
    fullname = MorakhsiDetailView.objects.filter()
    template = loader.get_template('app1/morakhasi.html')
    context = {
            'fullname':fullname,
    }
    return HttpResponse(template.render(context, request))








# =====================================================
# home
def home(request):
        all_personel = PersonalInfromation.objects.all().order_by('-created_at')
        return render(request,'app1/information_p.html',{"personels":all_personel})
# add personel
def add_personel(request):
        if request.method == "POST":
                if request.POST.get('fullname') \
                        and request.POST.get('jensiyat') \
                        and request.POST.get('semat') \
                        and request.POST.get('start_date') \
                        and request.POST.get('vaziyat') \
                        or request.POST.get('farzand'):
                        personel = PersonalInfromation()
                        personel.fullname = request.POST.get('fullname')
                        personel.jensiyat = request.POST.get('jensiyat')
                        personel.semat = request.POST.get('semat')
                        personel.start_date = request.POST.get('start_date')
                        personel.vaziyat = request.POST.get('vaziyat')
                        personel.farzand = request.POST.get('farzand')
                        personel.save()
                        return HttpResponseRedirect('/')
        else:
                return render(request,'app1/addpersonel.html')

# views peresonel
def personel(request,personel_id):
        personel = PersonalInfromation.objects.get(id = request.POST.get('id'))
        if personel != None:
                personel.fullname = request.POST.get('fullname')          
                personel.jensiyat = request.POST.get('jensiyat')          
                personel.semat = request.POST.get('semat')          
                personel.start_date = request.POST.get('start_date')          
                personel.vaziyat = request.POST.get('vaziyat')          
                personel.farzand = request.POST.get('farzand')
                personel.save()          
                return HttpResponseRedirect('/')

# Delete personel

def delete_personel(request,personel_id):
        personel = PersonalInfromation.objects.get(id = personel_id)
        personel.delete()
        return HttpResponseRedirect('/')
                        









# =====================================================

def hozorqiab(request):
        fullname = PersonelPresenceAbsence.objects.filter()
        template = loader.get_template('app1/hozor_qiab.html')
        context = {
                'fullname':fullname
        }
        return HttpResponse(template.render(context,request))


