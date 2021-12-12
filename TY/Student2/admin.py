from django.contrib import admin
from .models import Student_information, Student_Score

# Register your models here
class Student_informationAdmin(admin.ModelAdmin):
    list_display=['first_name', 'last_name', 'reg_number' , 'roll_number', 'Python', 'TOC', 'DBMS', 'OS']
    
    admin.site.register(Student_information)



class Student_ScoreAdmin(admin.ModelAdmin):
    list_display=['Python', 'TOC', 'DBMS', 'OS']
    
    admin.site.register(Student_Score)


 

