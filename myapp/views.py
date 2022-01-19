from datetime import date
from django.db.models.fields import DateField
from django.shortcuts import render
from .models import reg
from .forms import regform
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.



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
           obj_sign=reg.objects.get(email=email)
           
           if obj_sign.password == password:
               
               request.session['id'] = obj_sign.id
                       
               return redirect('/user/')
        
    except Exception as e:print(e)    
    return render(request,'signin.html')


def User(request):

    userid=request.session['id']  
    user_de=reg.objects.get(id=userid)
    
    if request.method == "POST":
        
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        mobile= request.POST['mobile']
        
        user=reg.objects.filter(id=userid).update(firstname=firstname,lastname = lastname ,email=email, password= password,mobilenumber=mobile)
        
    return render(request,'user.html',{"user":user_de})



def DeleteUser(request,userid):

    user=request.session['id']
    User=reg.objects.get(id=user)
    User.delete()  

    return redirect('/signin/')







