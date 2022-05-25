from django.contrib import admin
from .models import ForgetPassword, RelatedImage, User, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(User)
admin.site.register(RelatedImage)
admin.site.register(ForgetPassword)