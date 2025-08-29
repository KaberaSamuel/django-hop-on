from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200, default="")
    last_name = models.CharField(max_length=200, default="")
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200, default="")
    profile_image = models.CharField(max_length=200, default="") 

    def __str__(self):
        return self.email