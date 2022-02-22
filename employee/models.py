from django.db import models

class Employee(models.Model):
    ename = models.CharField(max_length=20)
    eage = models.IntegerField()
    eemail = models.EmailField()
    econtact = models.IntegerField()

    class Meta:
        db_table = 'employee1'
