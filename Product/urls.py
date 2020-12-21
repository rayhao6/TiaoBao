from django.urls import path

from . import views


app_name = 'Product'

urlpatterns = [
    path('', views.index, name='index'),
    #path('all', views.showAll, name='showAll'),
    path('detail', views.detail, name='detail'),

    path('<int:goodid>/add', views.addToCart, name='addToCart')
]