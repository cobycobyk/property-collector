from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('properties/', views.properties_index, name='property_index'),
  path('properties/<int:property_id>/', views.properties_detail, name='property_detail')
]