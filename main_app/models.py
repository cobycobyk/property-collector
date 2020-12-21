from django.db import models
from django.urls import reverse
from datetime import date

SHOWINGS = (
  ('M', 'Morning'),
  ('N', 'Noon'),
  ('A', 'Afternoon')
)
# Create your models here.
class Buyer(models.Model):
  name = models.CharField(max_length=50)
  number = models.CharField(max_length=11)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('buyers_detail', kwargs={'pk': self.id})

class Property(models.Model):
  street = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2)
  type = models.CharField(max_length=50)
  units = models.CharField(max_length=4)
  price = models.CharField(max_length=15)
  description = models.TextField(max_length=550)
  link = models.CharField(max_length=150)
  buyers = models.ManyToManyField(Buyer)

  def __str__(self):
    return self.street
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'property_id': self.id})

class Showing(models.Model):
  date = models.DateField('showing date')
  showing = models.CharField(max_length=1, choices=SHOWINGS, default=SHOWINGS[0][0])
  property = models.ForeignKey(Property, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_showing_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']