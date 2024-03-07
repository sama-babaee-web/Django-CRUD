from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from crud2.models import Candidate
from django.contrib.messages.views import SuccessMessageMixin  # get the in (add / edit)
from  django.contrib import messages  #Ussing to delete   
  
# (C) CREATE
class Create(SuccessMessageMixin,CreateView):
    model=Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')
    success_message = "Candidate: %(name)s created successfully !"
    
# (R) READ
class Read(ListView):
    model = Candidate
    queryset = Candidate.objects.all()

# (U) UPDATE
class Update(SuccessMessageMixin,UpdateView):
    model = Candidate
    fields = '__all__'
    success_url = reverse_lazy('read')
    success_message = "Candidate: %(name)s update successfully !"

# (D) DELETE

class Delete(DeleteView):
    # queryset = Candidate.objects.all()
    # success_url = reverse_lazy('read')
    model = Candidate
    def get_success_url(self):
        messages.success(self.request,"Candidate deleted successfully !")
        return reverse("read")