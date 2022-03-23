from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100)
    populations = models.IntegerField()
    area = models.IntegerField(null=True)
    
    class Meta():
        db_table = "city123"
    
class City123(models.Model):
    name = models.CharField(max_length=100)
    populations = models.IntegerField()
    area = models.IntegerField(null=True)
    
    class Meta():
        db_table = "sity"    