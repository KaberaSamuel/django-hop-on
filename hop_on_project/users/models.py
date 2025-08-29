from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="")
    phone_number = models.CharField(max_length=200, default="")
    profile_image = models.CharField(max_length=200, default="") 

    def __str__(self):
        return self.first_name