from django.db import models

# Create your models here.
class Hr(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.IntegerField()
    
    class Meta():
        db_table = 'hr'

        
