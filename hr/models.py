from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    employee_id = models.CharField(max_length=20, unique=True)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    date_hired = models.DateField()
    salary = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.employee_id} - {self.user.get_full_name() if self.user else 'No user'}"
