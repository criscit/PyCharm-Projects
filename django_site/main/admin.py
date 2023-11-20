from django.contrib import admin
from .models import Appointment


# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    # list_display = ['first_name', 'email']
    list_display = [field.name for field in Appointment._meta.fields]
    # exclude = ["email"]

    class Meta:
        model = Appointment


admin.site.register(Appointment, AppointmentAdmin)
