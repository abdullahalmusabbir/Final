from django.db import models

# Create your models here.

class users(models.Model):
    user_id=models.CharField(max_length=11)
    phone_number=models.CharField(max_length=11)
    user_name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    is_seller=models.BooleanField()
    
    def __str__(self):
        return self.user_id, self.user_name, self.email, self.phone_number

class seller(models.Model):
    user_id=models.ForeignKey(users, null=True, blank=True, on_delete=models.CASCADE)
    business_name=models.CharField(max_length=100)
    business_location=models.CharField(max_length=100)
    NID_number=models.CharField(max_length=100)
    verified=models.BooleanField()
    
    def __str__(self):
        return self.business_name, self.business_location    