from ast import keyword
from distutils.command.upload import upload
import email
from operator import mod
from pyexpat import model
from telnetlib import STATUS
from django.db import models

# Create your models here.

class Setting(models.Model):
    STATUS =(
        ('True','True'),
        ('False','False'),
    )
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = models.TextField()
    address = models.TextField()
    phone = models.IntegerField(blank=True,max_length=50)
    fax = models.CharField(blank=True,max_length=50)
    email = models.EmailField(blank=True, null=True,max_length=50)
    smtpserver = models.CharField(blank=True,null=True,max_length=100)
    smtpemail = models.CharField(blank=True,null=True,max_length=100)
    smtppassword = models.CharField(blank=True,max_length=100)
    smtpport = models.CharField(blank=True,max_length=100)
    icon = models.ImageField(blank=True, null=True, upload_to="icon/")
    facebook = models.CharField(blank=True, max_length=100)
    instagram = models.CharField(blank=True, max_length=100)
    contact = models.TextField()
    reference = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title