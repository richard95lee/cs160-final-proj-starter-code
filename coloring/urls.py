from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('bedroom', views.bedroom, name='bedroom'),
    path('viewdesign', views.viewdesign, name='viewdesign'),
]
