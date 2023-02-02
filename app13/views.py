from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Register,Image
from . forms import RegisterForm,LoginForm,UploadImageForm,UpdateForm
from django.contrib import messages
from django.contrib.auth import logout
def hello(request):
    return HttpResponse("welcome")
def index13(request):
    return render(request,'index.html')
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            place=form.cleaned_data['Place']
            age=form.cleaned_data['Age']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['ConfirmPassword']
            user=Register.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,'user already exists')
                return redirect('/register')
            elif password!=cpassword:
                messages.warning(request,'password mismatch')
                return redirect('/register')
            else:
                tab=Register(Name=name,Place=place,Age=age,Email=email,Password=password)
                tab.save()
                messages.success(request,'success')
                return redirect('/register')
    else:
        form=RegisterForm()
    return render(request,'register.html',{'data':form})
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Register.objects.get(Email=email)
                if not user:
                    messages.warning(request,'invalid user')
                    return redirect('/login')
                elif password!=user.Password:
                    messages.warning(request,'incorrect password')
                    return redirect('/login')
                else:
                    messages.success(request,'success')
                    return redirect('/home/%s' % user.id)
            except:
                messages.warning(request,'password or username incorrect')
                return redirect('/login')
    else:
        form=LoginForm()
    return render(request,'login.html',{'data':form})
def home(request,id):
    user=Register.objects.get(id=id)
    return render(request,'home.html',{'data':user})
def uploadimage(request):
    if request.method=='POST':
        form=UploadImageForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request,'upload successfully')
            return redirect('/')
            
    else:
        form=UploadImageForm()
    return render(request,'uploadimage.html',{'data':form})
def gallery(request):
    images=Image.objects.all()
    return render(request,'gallery.html',{'data':images})

def displayimg(request,id):
    im=Image.objects.get(id=id)
    return render(request,'displayimg.html',{'data':im})


def update(request,id):
    user=Register.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'success')
            return redirect('/home/%s' % user.id)
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'data':form,'user':user})
def logouts(request):
    logout(request)
    messages.success(request,'logout successfully')
    return redirect('/')
    
    