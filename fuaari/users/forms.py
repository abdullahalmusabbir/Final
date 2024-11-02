from django import forms 
from .models import *

class UserForms(forms.ModelForm):
    class Meta:
        model=users
        fields=['user_id','user_name','phone_number','email','password']
        
class SellerForm(forms.ModelForm):
    class Meta:
        model=seller
        fields=['business_name','business_location','NID_number']        