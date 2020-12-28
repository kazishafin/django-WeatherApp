from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=25, unique=True)
    def __str__(self):
        return self.name 
    
    def clean(self):
        self.name = self.name.capitalize()
    
    class Meta:
        verbose_name_plural = ('Cities')
        
        
        
    