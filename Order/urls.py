from django.urls import path

from . import views


app_name='Order'
urlpatterns = [
    path('', views.index, name='index'),
    path('orderdetail', views.getDetail, name='getDetail'),
    path('payment', views.payment, name='payment'),
    path('<int:Orderid>/deleteOrder', views.deleteOrder, name='deleteOrder')
]