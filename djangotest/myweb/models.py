from django.db import models

# Create your models here.


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=32,null=False)
    pwd = models.CharField(max_length=64)
    age = models.IntegerField()


class Department(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)


class Hosts(models.Model):
    hostname = models.CharField(max_length=32)
    ip = models.CharField(max_length=32,default='1.1.1.1')
    depart = models.ForeignKey(to='Department',to_field='id',default=1)