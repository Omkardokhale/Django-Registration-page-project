from django.shortcuts import render
from student1.models import Author, Entry, Blog
# Create your views here.


def view_hello1(request):
     
    stud_hello1 = Author.objects.all()

    # return render(request,'record.html',{'stud12':stud_record})
    return render(request,'hello1.html',{'stud1':stud_hello1})


def view_hello1(request):
     
    stud_hello1 = Entry.objects.all()

    # return render(request,'record.html',{'stud12':stud_record})
    return render(request,'hello1.html',{'stud2':stud_hello1})

def view_hello1(request):
     
    stud_hello1 = Blog.objects.all()

    # return render(request,'record.html',{'stud12':stud_record})
    return render(request,'hello1.html',{'stud3':stud_hello1})

