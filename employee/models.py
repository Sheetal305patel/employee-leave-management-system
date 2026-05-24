from django.db import models

class Leave(models.Model):

    employee_name = models.CharField(max_length=100)

    employee_email = models.EmailField()

    leave_reason = models.TextField()

    from_date = models.DateField()

    to_date = models.DateField()

    status = models.CharField(
        max_length=20,
        default='Pending'
    )

    def __str__(self):

        return self.employee_name