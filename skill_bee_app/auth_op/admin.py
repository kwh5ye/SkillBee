from django.contrib import admin

from auth_op.models import StudentUser, ClientUser

#from rango.models import Category, Page, UserProfile

admin.site.register(StudentUser)
admin.site.register(ClientUser)
