from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.

class Account(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    premium = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            # This is a new instance, so hash the password
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
