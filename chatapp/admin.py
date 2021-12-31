from django.contrib import admin
from . models import registration,Room,chatdata
# Register your models here.
class Registrationadmin(admin.ModelAdmin):
    list=['name','email','mobile','password']

admin.site.register(registration,Registrationadmin)
admin.site.register(Room)
admin.site.register(chatdata)
