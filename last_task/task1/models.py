from django.db import models
from django.db.models import (
    CharField, DecimalField, 
    IntegerField, TextField, BooleanField, 
    ManyToManyField)

# Create your models here.
class Buyer(models.Model):
    name = CharField(max_length=50)
    balance = DecimalField(max_digits=10, decimal_places=3)
    age = IntegerField()
    
    def __str__(self):
        return self.name
    
class Game(models.Model):
    title = CharField(max_length=100)
    cost = DecimalField(max_digits=15, decimal_places=3)
    size = DecimalField(max_digits=15, decimal_places=3)
    description = TextField()
    age_limit = BooleanField(default=False)
    buyer = ManyToManyField(Buyer, related_name='games')
    
    def __str__(self):
        return self.title, self.description, self.cost