from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def user(request):
    return render(request, ('user/user.html'))

def create_user(request):
    if request.method=='POST':
        form=UserForms(request.POST)
        if form .is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForms()
    return render (request, 'user/form.html',{'form':form})  

def user_list(request):
    user=users.objects.all()
    return render(request,'user/list.html',{'user':user}) 

def edit_user(request,pk):
    user=users.objects.get(pk=pk)
    if request.method=='POST':
        form=UserForms(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form=UserForms(instance=user)
    return render(request, 'user/edit_user.html',{'form':form})

def delete_user(request,pk):
    user=users.objects.all()
    if request.method=='POST':
        user.delete()
        return redirect('usr_list')
    return render(request, 'user/delete_user.html',{'user':user})
             