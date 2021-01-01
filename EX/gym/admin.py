from django.contrib import admin
from .models import Course, Coach, User, Locker, PhyTest

# Register your models here.
admin.site.register(Course)
admin.site.register(Coach)
admin.site.register(User)
admin.site.register(Locker)
admin.site.register(PhyTest)


