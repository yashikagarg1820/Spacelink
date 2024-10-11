from django.db import models
from django.contrib.auth.hashers import make_password, check_password
# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)


#Registration data model
class Registration(models.Model):
    username = models.CharField(max_length=50)
    phone_number=models.IntegerField()
    email_id=models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)