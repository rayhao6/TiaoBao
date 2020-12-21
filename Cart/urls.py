from django.urls import path

from . import views


app_name='Cart'
urlpatterns = [
    path('', views.index, name='index'),
    path('TotalPrice', views.getTotalPrice, name='getTotalPrice'),
    path('<int:goodid>/add', views.addToCart, name='addToCart'),
    path('<int:goodid>/delete', views.deleteInCart, name='deleteInCart'),
    path('deleteAll', views.deleteAllCart, name='deleteAll'),
    path('addToOrder', views.addToOrder,name='addToOrder'),
    path('<int:goodid>/deleteone', views.deleteone, name='deleteAll'),

]