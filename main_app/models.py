from django.db import models

# Create your models here.
class Property(models.Model):
  street = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=2)
  type = models.CharField(max_length=50)
  units = models.CharField(max_length=4)
  price = models.CharField(max_length=15)
  description = models.TextField(max_length=550)
  link = models.CharField(max_length=150)

  def __str__(self):
    return self.street