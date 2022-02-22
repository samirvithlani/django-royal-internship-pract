from telnetlib import STATUS
from django.db import models

class Exam(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.BooleanField(default=True)

    class Meta():
        db_table = 'exam'
    
