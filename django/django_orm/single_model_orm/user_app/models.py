from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    gender=models.TextField()
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.
#User.objects.create(first_name="moh",last_name="dd",email="m@gmail.com",age="24")
# User.objects.create(first_name="sami",last_name="bb",email="s@gmail.com",age="25")
# User.objects.create(first_name="hasan",last_name="ss",email="h@gmail.com",age="26")