from django.urls import path
from app2 import views

app_name = 'app2'

urlpatterns = [
    path('', views.NumberFormView.as_view(), name='modal'),
    path('form/', views.form_test, name='form_test'),
]