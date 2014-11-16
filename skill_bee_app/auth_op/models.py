from django.db import models
from django.contrib.auth.models import User

import datetime
from django.utils import timezone

class StudentUser(models.Model):
    # Includes USERNAME, PASSWORD, EMAIL ADDRESS, FIRST NAME, LAST NAME
    user = models.OneToOneField(User)

    picture = models.ImageField(upload_to='profile_images', blank=True)

    major = models.TextField()
    grad_year = models.PositiveSmallIntegerField()
    gpa = models.FloatField()
    portfolio = models.TextField(blank=True)
    app_bool = models.BooleanField(default=False)
    sup_bool = models.BooleanField(default=False)
    soc_bool = models.BooleanField(default=False)

    def __unicode__(self):  # Python 3: def __str__(self):
        return str(self.user) + "\nMajor, Grad, GPA, Porf " + str(self.major) + str(self.grad_year) + str(self.gpa) + str(self.portfolio)

class ClientUser(models.Model):
    # Includes USERNAME, PASSWORD, EMAIL ADDRESS, FIRST NAME, LAST NAME
    user = models.OneToOneField(User)

    phone_number = models.TextField()
    organization = models.TextField(blank=True)

    def __unicode__(self):
      return str(self.user) + "\nPhone #, Org " + str(self.phone_number) + str(self.organization)
