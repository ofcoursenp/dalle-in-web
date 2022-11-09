from django.db import models

# Create your models here.
class InputHm(models.Model):
    name = models.CharField(null=True,max_length=300)
    
    def __str__(self):
        return self.name
