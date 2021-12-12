from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Student_information(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)  
    reg_number = models.CharField(max_length=20)
    roll_number = models.CharField(max_length=20)
    Python = models.CharField(max_length=30)  
    TOC = models.CharField(max_length=30)  
    DBMS = models.CharField(max_length=30)  
    OS = models.CharField(max_length=30)  
  
    def _str_(self):
        return self.first_name

    def _str_(self):
        return self.last_name

    def _str_(self):
        return self.reg_number

    def _str_(self):
        return self.roll_number