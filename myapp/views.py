from django.shortcuts import render,redirect
from .form import StudentRagistation
from .models import User



def index(request):
    print('dfdfd')
    stu = User.objects.all()

    return render(request, 'index.html',{'stu': stu})

def add_student(request):
    if request.method == 'POST':
        fm = StudentRagistation(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentRagistation()

    return render(request, 'add.html', {'fm': fm})

def edit_student(request,id=None):

    userid =User.objects.get(id=id)
    fm = StudentRagistation(request.POST or None, instance=userid)
    if fm.is_valid():
        fm.save()
        return redirect('/')
    return render(request,'edit.html',{'fm': fm})

def delete_student(request,id=None):

    userid = User.objects.get(id=id)
    if 'del' in request.POST:
        userid.delete()
        return redirect('/')
    return render(request,'delete.html')

def home(request):
    return render(request,'home.html')


