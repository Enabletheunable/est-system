from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Project(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    budget_amount = models.DecimalField(max_digits=20, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[
            ('planning', 'Planning'),
            ('active', 'Active'),
            ('completed', 'Completed')
        ],
        default='planning'
    )
    project_manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects_app_projects'  # unique reverse name to avoid clash
    )

    def __str__(self):
        return f"{self.code} - {self.name}"
