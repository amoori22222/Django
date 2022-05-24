from django.contrib import admin
from .models import Service, Project, Contact

# Register your models here.
admin.site.register((Service, Project, Contact))
