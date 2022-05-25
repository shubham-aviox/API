from django.contrib import admin
from .models import UnivStudent, User

# Register your models here.
admin.site.register(User)
admin.site.register(UnivStudent)