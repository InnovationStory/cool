from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django.utils.html import escape, mark_safe
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.forms import ModelForm
from django.utils.text import slugify
from django.template.defaultfilters import slugify
from django.dispatch import receiver
import re
from django.utils import timezone
from djrichtextfield.widgets import RichTextWidget
from djrichtextfield.models import RichTextField


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name





class Universite(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Domaine(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name



class Student(models.Model):

    name = models.CharField(max_length=270,verbose_name= u"Last name  ")
    prenom = models.CharField(max_length=270,verbose_name= u"First name   ")
    adresse_email = models.EmailField(max_length=100,verbose_name=u"email ",)
    numero_telephone=models.IntegerField(verbose_name= u"Phone number  ",  null=True, blank=True)
    composante = models.ManyToManyField(Universite, verbose_name= u"University  ", related_name='universty_student')
    domaine = models.CharField(max_length=100,verbose_name=u"Scientific background  ", help_text="(engineering, marketing, computing science,  mechanics....)")
    fonction = models.ManyToManyField(Subject, verbose_name= u"Function  ", related_name='interested_student')
    autre = models.CharField(max_length=270,verbose_name= u"If other ",  null=True, blank=True)
    choice_field = models.CharField(max_length=270,verbose_name= u" ",  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null= True)
    name_adre = models.CharField(max_length=270,verbose_name= u"I want to work with (First and last Name) ", help_text=" PS: you can only choose one Person to work with",  null=True, blank=True)
    prenom_adre = models.CharField(max_length=270,verbose_name= u"First name   ", null=True, blank=True)
    adresse_email_adre = models.EmailField(max_length=100,verbose_name=u"Email address of the person you want to work with.",null=True, blank=True)
    description = models.TextField(max_length=100000, verbose_name=u"Motivation  ", help_text="What are your motives for applying to this e-workshop?")



    def __str__(self):
        if self.name==None:
           return "ERROR-CUSTOMER NAME IS NULL"
        return self.name

