from django.contrib import admin
from .models import Booking, Menu

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
  pass

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
  pass