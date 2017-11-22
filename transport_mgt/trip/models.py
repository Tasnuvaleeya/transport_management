from django.db import models


class SignUp(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    contact = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    confirm_password = models.CharField(max_length=20)
    house_name = models.CharField(max_length=20)
    street = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.first_name)
