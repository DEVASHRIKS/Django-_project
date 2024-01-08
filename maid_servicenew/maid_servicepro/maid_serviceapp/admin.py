from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customer_Register)
admin.site.register(Serviceman_Register)
admin.site.register(Login)
admin.site.register(Service_Category)
admin.site.register(Service_City)
admin.site.register(Booking_Data)