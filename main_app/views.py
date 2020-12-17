from django.shortcuts import render
from .models import Property

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def properties_index(request):
  properties = Property.objects.all()
  return render(request, 'properties/properties_index.html', {'properties': properties})

def properties_detail(request, property_id):
  property = Property.objects.get(id=property_id)
  return render(request, 'properties/properties_detail.html', {'property': property})