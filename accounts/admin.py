from django.contrib import admin
from .models import Role, Department, User

admin.site.register(Role)
admin.site.register(Department)
admin.site.register(User)