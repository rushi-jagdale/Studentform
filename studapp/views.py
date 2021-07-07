from django.shortcuts import redirect, render
from .models import Student
from django.contrib import messages 


# Create your views here.
def add(request):
   if request.method == 'POST':

        
       name = request.POST['name']
       age = request.POST['age']
       gender = request.POST['gender']
    #    if Student.objects.filter(name = name).exists():
    #             messages.info(request, 'name already taken..')
               
    #             return redirect('add')

       data = Student.objects.create(name=name,age=age,gender=gender)
       data.save()
       messages.info(request, 'Student Created Successfully....')

       return redirect('add')
      

   else:
        return render(request,'add.html')

def show(request):
    data = Student.objects.all()
    return render(request,'show.html',{'data':data})
