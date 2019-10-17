from django.contrib import admin

# import blog model 
from .models import Blog

# Register your models here.
admin.site.register(Blog)
