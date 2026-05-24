from django.contrib import admin
from .models import Leave

@admin.register(Leave)

class LeaveAdmin(admin.ModelAdmin):

    list_display = (
        'employee_name',
        'employee_email',
        'from_date',
        'to_date',
        'status'
    )