from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comp_name = models.CharField(max_length=50)
    gst = models.IntegerField()
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.comp_name
    
class Service(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.IntegerField()
    amount = models.IntegerField()

    def __str__(self):
        return self.description
    
class Add_service(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, blank=True, null=True)
    comp2_name = models.CharField(max_length=50)
    handle_by = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.IntegerField()
    account = models.IntegerField()

    def __str__(self):
        return self.comp2_name