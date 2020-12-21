from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Property, Buyer
from .forms import ShowingForm

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
  buyers_property_doesnt_have = Buyer.objects.exclude(id__in = property.buyers.all().values_list('id'))
  showing_form = ShowingForm()
  return render(request, 'properties/properties_detail.html', {'property': property, 'showing_form': showing_form, 'buyers': buyers_property_doesnt_have})

class PropertyCreate(CreateView):
  model = Property
  fields = '__all__'

class PropertyUpdate(UpdateView):
  model = Property
  fields = ['street', 'city', 'state', 'type', 'units', 'price', 'description', 'link']

class PropertyDelete(DeleteView):
  model = Property
  success_url = '/properties'

def add_showing(request, property_id):
  form = ShowingForm(request.POST)
  if form.is_valid():
    new_showing = form.save(commit=False)
    new_showing.property_id = property_id
    new_showing.save()
  return redirect('properties_detail', property_id=property_id)

def assoc_buyer(request, property_id, buyer_id):
  Property.objects.get(id=property_id).buyers.add(buyer_id)
  return redirect('properties_detail', property_id=property_id)

class BuyerList(ListView):
  model = Buyer

class BuyerDetail(DetailView):
  model = Buyer

class BuyerCreate(CreateView):
  model = Buyer
  fields = '__all__'

class BuyerUpdate(UpdateView):
  model = Buyer
  fields = '__all__'

class BuyerDelete(DeleteView):
  model = Buyer
  success_url = '/buyers/'
