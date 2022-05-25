from email.mime import image
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/product')
    price = models.IntegerField()
    description = models.CharField(max_length=150)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class RelatedImage(models.Model):
    relate_image = models.ImageField(upload_to='images/product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.relate_image


class User(AbstractUser):
    phone = models.CharField(max_length=12)


class ForgetPassword(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.verification_code