from django.contrib import admin
from .models import Room , Topic , Message, User
# Register your models here.

# we are registering model to see in the admin panel
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
