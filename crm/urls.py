
from django.contrib import admin
from django.urls import path,include
from CURD import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app1.urls')),
    path('modal',include('app2.urls')),
    
    path('table',include('crud2.urls')),
    
    
    # app CURD ============>
    path('',views.home,name="home"),
    # Add product
    path('add_product',views.add_product,name="add_product"),
    # views the product individually
    path('product/<str:product_id>',views.product,name="product"),
    # Edit product
    path('edit_product',views.edit_product,name="edit_product"),
    # Delete product
    path('delete_product/<str:product_id>',views.delete_product,name="delete_product"),
    
    
    
]
