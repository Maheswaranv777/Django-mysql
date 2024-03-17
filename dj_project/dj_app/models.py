from django.db import models

class Tech(models.Model):
    s_no=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=45,unique=True)
    course=models.CharField(max_length=20)
