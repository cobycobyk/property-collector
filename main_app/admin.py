from django.contrib import admin
from .models import Property, Showing, Buyer

# Register your models here.
admin.site.register(Property)
admin.site.register(Showing)
admin.site.register(Buyer)