from django.shortcuts import render
from Student2.models import Student_information


# Create your views here.
def view_hello(request):
    stud_record = Student_information.objects.all()
    return render(request,'hello.html',{'stud12':stud_record})




