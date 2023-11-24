from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('entry/getdata/', views.getdata, name="getdata"),
    path('entry/getdata/final/',views.final,name='final'),
    path('entry/new', views.new, name='new')

]
