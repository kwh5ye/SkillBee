from django.contrib import admin

from login.models import StudentUser, ClientUser

#from rango.models import Category, Page, UserProfile

admin.site.register(StudentUser)
admin.site.register(ClientUser)
