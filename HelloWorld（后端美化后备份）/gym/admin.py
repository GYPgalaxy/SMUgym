from django.contrib import admin
from .models import User, Coach, Course, Locker, PhyTest


# Register your models here.
admin.site.register(User)
admin.site.register(Coach)
admin.site.register(Course)
admin.site.register(Locker)
admin.site.register(PhyTest)