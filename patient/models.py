from __future__ import unicode_literals
from __future__ import unicode_literals
from  django.utils import *
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Patients(models.Model):
    sex = (
        (u'MALE', u'MALE'),
        (u'FEMALE', u'FEMALE'),
        (u'OTHERS', u'OTHERS'),
    )
    firstname=models.CharField(max_length=50,null=False,blank=False,default="anonymous_user_fname")
    lastname = models.CharField(max_length=50, null=False, blank=False, default="anonymous_user_lname")
    age=models.IntegerField(null=False,blank=False,default=0)
    dob=models.DateField(null=False,blank=False,default=datetime.now)
    gender=models.CharField(max_length=6,choices=sex,null=False,default='MALE',blank=False)
    mobile=models.CharField(max_length=14,null=False,blank=False,default="anonymous_mobile")
    comment=models.CharField(max_length=540,null=False,blank=False,default="anonymous_COMMENT")
    reg_date = models.DateTimeField(null=False, blank=False, default=datetime.now)

    def __unicode__(self):
        return self.firstname
