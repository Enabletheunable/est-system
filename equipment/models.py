from django.db import models

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    purchase_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[('available','Available'),('in_use','In Use'),('maintenance','Maintenance')]
    )
    assigned_to = models.ForeignKey('hr.Employee', on_delete=models.SET_NULL, null=True, blank=True)
    last_service_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
