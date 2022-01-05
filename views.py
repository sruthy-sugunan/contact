from django.shortcuts import render,redirect
from .models import Contact
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from contact_book.settings import EMAIL_HOST_USER

# Create your views here.
@login_required
def homee(request):
    return render(request,'page.html')


	

def loginview(request):
    uname = request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('homee')
    else:
        return render(request,"login.html")

def logout_view(request):
    logout(request)
    return redirect('login')





def sign_up(request):
        form = UserCreationForm(request.POST)
        if request.method == "POST":
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('uname')
                password = form.cleaned_data.get('password1')
                user = authenticate(request, username=username, password=password)
                return redirect('homee')

                #if user is not None:
                 #   login(request,user)
                 #   return redirect('home')
                #else:
                 #    return render(request,"registration/sign_up.html")



        else:
            form = UserCreationForm()
        return render(request, 'registration/sign_up.html', {'form': form})
        
                   
         
        


def Resethome(request):
    return render(request,'registration/ResetPassword.html')

def resetPassword(request):
    responseDic={}
    try:
        username = request.POST['uname']
        recepient=request.POST['email']
        pwd=request.POST['password']
        subject="Password reset"
        try:
            user=User.objects.get(username=username)
            if user is not None:
                user.set_password(pwd)
                user.save()
                message="Your password was changed"
                send_mail(subject,message, EMAIL_HOST_USER, [recepient])
                responseDic["errmsg"]="Password Reset Successfully"
                return render(request,"registration/ResetPassword.html",responseDic)
        except Exception as e:
            print(e)
            responseDic["errmsg"]="Email doesnt exist"
            return render(request,"registration/ResetPassword.html",responseDic)
        
    except Exception as e:
        print(e)
        responseDic["errmsg"]="Failed to reset password"
        return render(request,"registration/ResetPassword.html",responseDic)


def index(request):
    return render(request,"page.html")

def hom(request):
    return render(request,"home.html")




def home(request):
    try:
        Name=request.POST['name']
        Number=request.POST['ph']
        cnlist=Contact.objects.get(name=Name)
        if cnlist is not None:
            return render(request,"home.html",{"msg":"Name already existed!"})

    except Exception as e:
        print(e)
        contactlist=Contact(name=Name,number=Number)
        contactlist.save()
        return redirect('view')

        

   
            

def view(request):
    contactlist=Contact.objects.all()
    return render(request,'view.html',{'det':contactlist})


def update(request):
    return render(request,"update.html")




def nameupdate(request):
    try:
        Oldname=request.POST.get('oname')
        Newname=request.POST.get('nname')
        cnlist=Contact.objects.get(name=Oldname)
        if cnlist is not None:
           Contact.objects.filter(name=Oldname).update(name=Newname)
           return render(request,"update.html",{"msg":"Name Updated"})
    except Exception as e:
        print(e)
        return render(request,"update.html",{"sg":"Name not in list!"})




def numupdate(request):
    try:
        Name=request.POST['name']
        Number=request.POST['nnum']
        cnlist=Contact.objects.get(name=Name)
        if cnlist is not None:
          Contact.objects.filter(name=Name).update(number=Number)
          return render(request,"update.html",{"msg":"Number Updated"})
    except Exception as e:
        print(e)
        return render(request,"update.html",{"sg":"Name not in list!"})



def dele(request):
    return render(request,"delete.html")



def delete(request):
    try:
        Name=request.POST.get('name')
        cnlist=Contact.objects.get(name=Name)
        if cnlist is not None:
           contactdtl=Contact.objects.filter(name=Name)
           contactdtl.delete()
           return render(request,"delete.html",{"msg":"Deleted successfully!"})
    except Exception as e:
        print(e)
        return render(request,"delete.html",{"msg":"Name not in list!"})




   

    

