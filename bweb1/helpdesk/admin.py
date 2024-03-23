from django.contrib import admin
from .models import Users, Tickets, Messages

# Register your models here.
admin.site.register(Tickets)
admin.site.register(Users)
admin.site.register(Messages)