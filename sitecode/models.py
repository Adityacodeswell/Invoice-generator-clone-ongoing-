from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=50)
    gst = models.CharField(max_length=15)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.comp_name
    
class Service(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Example for decimal field

    def __str__(self):
        return self.description
    

class AddClient(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    comp2_name = models.CharField(max_length=50)
    handle_by = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    account = models.CharField(max_length=20)
    ifsc = models.CharField(max_length=20)
    bank = models.CharField(max_length=40)
    gst = models.CharField(max_length=15)

    def __str__(self):
        return self.comp2_name
    
    class Meta:
        db_table = 'providers'






