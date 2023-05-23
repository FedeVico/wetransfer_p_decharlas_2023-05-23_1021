from django.contrib import admin

from .models import Message, User, Room, Password, Room_Register, Room_Vote

admin.site.register(Message)
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Password)
admin.site.register(Room_Register)
admin.site.register(Room_Vote)



# Register your models here.
