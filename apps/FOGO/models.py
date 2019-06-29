from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 60)
    password = models.CharField(max_length = 60)
    admin_flag = models.IntegerField(default=0)

    street = models.CharField(max_length = 60)
    city = models.CharField(max_length = 60)
    state = models.CharField(max_length = 60)
    zipcode = models.IntegerField()
    aptnum = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

