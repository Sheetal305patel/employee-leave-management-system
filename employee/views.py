from django.shortcuts import render
from .models import Leave

def home(request):

    success = False

    if request.method == "POST":

        employee_name = request.POST.get('employee_name')

        employee_email = request.POST.get('employee_email')

        leave_reason = request.POST.get('leave_reason')

        from_date = request.POST.get('from_date')

        to_date = request.POST.get('to_date')

        Leave.objects.create(

            employee_name=employee_name,

            employee_email=employee_email,

            leave_reason=leave_reason,

            from_date=from_date,

            to_date=to_date
        )

        success = True

    return render(request, 'index.html', {
        'success': True 
    })
