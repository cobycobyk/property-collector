from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('properties/', views.properties_index, name='properties_index'),
  path('properties/<int:property_id>/', views.properties_detail, name='properties_detail'),
  path('properties/create/', views.PropertyCreate.as_view(), name='properties_create'),
  path('properties/<int:pk>/update/', views.PropertyUpdate.as_view(), name='properties_update'),
  path('properties/<int:pk>/delete/', views.PropertyDelete.as_view(), name='properties_delete'),
  path('properties/<int:property_id>/add_showing/', views.add_showing, name='add_showing'),
  path('properties/<int:property_id>/assoc_buy/<int:buyer_id>/', views.assoc_buyer, name='assoc_buyer'),
  path('buyers/', views.BuyerList.as_view(), name='buyers_index'),
  path('buyers/<int:pk>/', views.BuyerDetail.as_view(), name='buyers_detail'),
  path('buyers/create/', views.BuyerCreate.as_view(), name='buyers_create'),
  path('buyers/<int:pk>/update/', views.BuyerUpdate.as_view(), name='buyers_update'),
  path('buyers/<int:pk>/delete/', views.BuyerDelete.as_view(), name='buyers_delete'),
]