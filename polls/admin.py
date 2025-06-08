from django.contrib import admin
#You need to import your models in order for them to be viewable by the admin
from .models import Question

# Register your models here.
admin.site.register(Question)