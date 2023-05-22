from django.contrib import admin

from .models import *
from django.contrib.auth.admin import Group, User

# Register your models here.

admin.site.register(Trainer)
admin.site.register(Post)
admin.site.register(Photo)
admin.site.register(Slider_Photo)
<<<<<<< HEAD
=======
admin.site.register(Address)

admin.site.unregister(User)
admin.site.unregister(Group)
>>>>>>> backend
