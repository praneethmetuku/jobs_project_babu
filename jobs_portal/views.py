from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from jobs_portal.models import Hydjobs,Punejobs,Blrjobs,Chennaijobs
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request,'home.html')

def hyd(request):
    list=Hydjobs.objects.order_by('date')
    dict_list={'hydjobs':list}
    return render(request,'hydjobs.html',context=dict_list)

def pune(request):
    list=Punejobs.objects.order_by('date')
    dict_list1={'punejobs':list}
    return render(request,'punejobs.html',context=dict_list1)

def chennai(request):
    list=Chennaijobs.objects.order_by('date')
    dict_list2={'chennaijobs':list}
    return render(request,'chennaijobs.html',context=dict_list2)

def blr(request):
    list=Blrjobs.objects.order_by('date')
    dict_list3={'blrjobs':list}
    return render(request,'blrjobs.html',context=dict_list3)

def contact(request):
    return render(request,'contact.html')

def login_user(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('you have successfully logged in'))
            return redirect('home')

        # Redirect to a success page.


        else:
            messages.success(request,('OOps something wrong'))

            return redirect('login')

        # Return an 'invalid login' error message.
    else:
        return render(request,'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,('babe you successfully logged out'))
    return redirect('home')


def register_user(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request,'babe you successfully registered')
            return redirect('home')

    else:
        form= UserCreationForm()
    context= {'form':form}

    return render(request,'register.html',context)
