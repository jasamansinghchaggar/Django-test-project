from django.db import models
from django.urls import reverse, reverse_lazy

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cbvApp:companydetail', kwargs={'pk': self.pk})
    
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employee')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cbvApp:companydetail', kwargs={'pk': self.company.pk})