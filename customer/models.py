from django.db import models

# Create your models here.

class Customer(models.Model):
    firstName = models.CharField(max_length  = 50)
    lastName = models.CharField(max_length = 50)
    emailID = models.EmailField(max_length = 50,unique = True)
    passWord = models.CharField(max_length = 20)
    photo = models.ImageField(upload_to='images')
    phoneNo = models.CharField(max_length = 10,blank = True)
    userCreatedAt = models.DateTimeField(auto_now_add = True)
    userUpdatedAt = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.firstName