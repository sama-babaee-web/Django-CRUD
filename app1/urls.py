from django.urls import path 
from . import views

urlpatterns = [
    path('morakhasi',views.morakhasi,name="morakhasi"),
    path('hozor',views.hozorqiab,name="hozorghiab"),
#   0000000000000000000000000000000000
    path('personel',views.home,name="inf-personel"),
    path('add_personel',views.add_personel,name="add_personel"),
    path('personel/<str:personel_id>',views.personel,name="personel"),
    # path('edit_personel',views.personel,name="edit_personel"),
    # path('delete_personel/<str:personel_id>',views.delete_personel,name="delete_personel"),

]
