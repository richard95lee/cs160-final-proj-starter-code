from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('main', views.main, name='main'),
    path('color1', views.color1, name='color1'),
    path('color2', views.color2, name='color2'),
    path('color3', views.color3, name='color3')
]
