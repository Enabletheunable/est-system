from django.db import models

class Expense(models.Model):
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return f"{self.project.name} - {self.amount}"

class Payment(models.Model):
    employee = models.ForeignKey('hr.Employee', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.employee.employee_id} - {self.amount}"
