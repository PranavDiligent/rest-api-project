
from django.db import models

# Create your models here.
class Student(models.Model):

    genders = (
        ('M','Male'),
        ('F','Female'),

    )

    name = models.CharField(max_length=50,blank=True,null=True)
    age = models.PositiveIntegerField(blank=True,null=True)
    gender = models.CharField( choices=genders,max_length=5,blank=True,null=True)
    

    def __str__(self):
        return self.name

    
