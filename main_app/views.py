from django.shortcuts import render

from django.http import HttpResponse

class Property:
  def __init__(self, street, city, state, type, units, price, description, link):
    self.street = street
    self.city = city
    self.state = state
    self.type = type
    self.units = units
    self.price = price
    self.description = description
    self.link = link
  
properties = [
  Property('2836 W 53rd Ave', 'Denver', 'CO', 'Apartment', '4', '2,040,000', "Beautiful new construction 4-plex now available for sale! Don't miss this unbeatable opportunity to own a fantastic cash-flowing asset. This 4-unit bundle offers over 6,000 sf of leasable area, 12 total bedrooms, and 16 total bathrooms. Take advantage of low interest rates and purchase this income generator. Aria townhomes are located between I-70 & I-76, across from the expanding Regis University and near ample amounts of public transit. Chaffee Park is one of the most up & coming, explosive neighborhoods in Northwest Denver. Purchase now while we're offering our limited summer time incentives, meet with our designers and hand select your finishes in each unit. Contact now for immediate details.", 'https://www.loopnet.com/Listing/2836-2848-W-53rd-Ave-Denver-CO/20418041/'),
  Property('3275 W Nevada Pl', 'Denver', 'CO', 'Apartment', '6', '999,500', "Built in 1963, this Multi-family property features six units with six available parking spaces.", 'https://www.loopnet.com/Listing/3275-W-Nevada-Pl-Denver-CO/16233736/'),
  Property('3531 S Pennsylania St - Penn Rows', 'Englewood', 'CO', 'Apartment', '12', '7,000,000', "Penn Rows is a 12-unit townhouse apartment community strategically located in Englewood, CO in Arapahoe County, across the street from the main entrance to Swedish Hospital to the north and a new 100,000-square-foot medical building with retail to the east. Constructed in 2020 and situated on 0.22 acres, the property is comprised of two, three-story building of two-bedroom / two- and onehalf bathroom units with spacious floor plans. Amenities include air conditioning, granite countertops, island kitchen, dishwasher, disposal, hardwood floors, washer and dryer hook-ups, and luxury finishes. A two-car garage for each unit and rooftop patios round out the amenity package.", 'https://www.loopnet.com/Listing/3531-3539-S-Pennsylvania-St-Englewood-CO/20206195/')
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def properties_index(request):
  return render(request, 'properties/properties_index.html', {'properties': properties})