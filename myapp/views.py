from datetime import date
from django.db.models.fields import DateField
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.


# STUDENT

def Reg(request):

    form=regform
    try:
        if request.method == "POST":

            form=regform(request.POST)  
            
            if form.is_valid():

                firstname = form.cleaned_data['firstname']
                lname = form.cleaned_data['lastname']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                mobilenumbe = form.cleaned_data['mobilenumber']

                obj=reg.objects.filter(email=email).exists()
                
                if obj==True:
                    messages.warning(request, 'This email address is already being used')                           
                else:
                    form.save()
                    return redirect('/signin/')
                                
    except Exception as e:print(e)                
    return render(request,'reg.html',{"form":form})



def Signin(request):

    try:
        if request.method == "POST":

           email = request.POST['email']
           password = request.POST['password']     
           
           try:
               obj_sign=reg.objects.get(email=email)
           except:       
               messages.warning(request, 'The email address or mobile number you entered isnt connected to an account')  
           
           if obj_sign.password == password:              
               request.session['id'] = obj_sign.id
               return redirect('/user/')
           
           else:
               messages.warning(request, 'user name or password incorrect')  
   
    except Exception as e:print(e)    
    return render(request,'signin.html')


def User(request):
    
    try:
        userid=request.session['id']  
        user_de=reg.objects.get(id=userid)
    
        if request.method == "POST":
      
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            mobile= request.POST['mobile']
        
            user=reg.objects.filter(id=userid).update(firstname=firstname,lastname = lastname ,email=email, password= password,mobilenumber=mobile)

    except Exception as e:print(e)    
        
    return render(request,'user.html',{"user":user_de})


def DeleteUser(request,userid):

    user=request.session['id']
    User=reg.objects.get(id=user)
    User.delete()  

    return redirect('/signin/')


def logout(request):
    try:
        del request.session['id']

    except KeyError:
        pass
    return  redirect('/signin/')



# COLLEGE

def clgreg(request):

    form=collegereg
    try:
        if request.method == "POST":

            form=collegereg(request.POST)  
            
            if form.is_valid():

                collegename = form.cleaned_data['collegename']
                location = form.cleaned_data['location']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                mobilenumber = form.cleaned_data['mobilenumber']

                obj=college_reg.objects.filter(email=email).exists()
                
                if obj==True:
                    messages.warning(request, 'This email address is already being used')                           
                else:
                    form.save()
                    return redirect('/collegesign/')
                                
    except Exception as e:print(e)                
    return render(request,'clgreg.html',{"form":form})


def ClgSign(request):
    
    try:
        if request.method == "POST":

           email = request.POST['email']
           password = request.POST['password']     
           
           try:
               obj_sign=college_reg.objects.get(email=email)
           except:       
               messages.warning(request, 'The email address or mobile number you entered isnt connected to an account')  
                 
           if obj_sign.password == password:              
               request.session['clid'] = obj_sign.id
               return redirect('/collegede/')      
           else:
               messages.warning(request, 'user name or password incorrect')  
   
    except Exception as e:print(e)    
    return render(request,'clgsignin.html')


def clgde(request):
    
    try:
        userid=request.session['clid']  
        user_de=college_reg.objects.get(id=userid)
    
        if request.method == "POST":
      
            collegename = request.POST['collegename']
            location = request.POST['location']
            email = request.POST['email']
            password = request.POST['password']
            mobile= request.POST['mobile']
        
            user=college_reg.objects.filter(id=userid).update(collegename=collegename, location =  location ,email=email, password= password,mobilenumber=mobile)

    except Exception as e:print(e)     
    return render(request,'clgdetails.html',{"user":user_de})


def ClDeleteUser(request,userid):

    user=request.session['clid']
    User=college_reg.objects.get(id=user)
    User.delete()  

    return redirect('/collegesign/')


def cllogout(request):
    
    try:
        del request.session['clid']

    except KeyError:
        pass
    return  redirect('/collegesign/')


# ADMIN

def admin(request):
    
    user=reg.objects.all()
    clg=college_reg.objects.all()

    return render(request,'admin.html',{'seeker':user,'clg':clg})


def Deuser(request,**kwargs):
   
    id=kwargs.get('userid') 
    user=reg.objects.get(id=id)
    user.delete()

    return redirect('/admin/')

def Declg(request,**kwargs):

    id=kwargs.get('clgid') 
    clg=college_reg.objects.get(id=id)
    clg.delete()

    return redirect('/admin/')

