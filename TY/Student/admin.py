from django.contrib import admin
from .models import Student_information

# Register your models here.
class Student_informationAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'reg_number' , 'roll_number', 'Python', 'TOC', 'DBMS', 'OS']


    admin.site.register(Student_information)