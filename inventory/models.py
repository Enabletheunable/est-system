from django.db import models

class Material(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    quantity = models.FloatField()
    unit = models.CharField(max_length=20)
    price_per_unit = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return f"{self.code} - {self.name}"

class MaterialUsage(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    quantity_used = models.FloatField()
    date_used = models.DateField()

    def __str__(self):
        return f"{self.material.name} for {self.project.name}"
