from django import forms
from django.forms import ModelForm
from django.forms import fields
from .models import *
from django.core.exceptions import ValidationError
from django.forms import EmailField
from django.core.validators import RegexValidator



class regform(forms.ModelForm):

    
    class Meta:
        
        model=reg
        fields='__all__'


    firstname = forms.CharField(label="firstname")
    lastname = forms.CharField(label="lastname")
    email = forms.EmailField(label="email")
    password = forms.CharField(label="password")
    mobilenumber = forms.CharField(validators=[RegexValidator(regex=r'^\+?1?\d{9,10}$', message="enter valid Phone number")])

    def clean(self):
        
        cleaned_data = super().clean()
        cc_myself = cleaned_data.get("firstname")
        email=cleaned_data.get("email")
        password=cleaned_data.get("password")
        
        if len(cc_myself) < 4:
            self._errors['firstname'] = self.error_class([
                'Minimum 5 characters required'])
        
        
        def isEmailAddressValid( semail ):
           
           try:
               EmailField().clean(semail)
               return True
                            
                         
           except ValidationError:
               return False
        if len(password)<8:
            self._errors['spassword'] = self.error_class([
                'Minimum 8 characters required'])

    