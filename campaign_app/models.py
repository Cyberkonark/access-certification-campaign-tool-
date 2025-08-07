from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    name = models.CharField(max_length=100)

class AccessEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    manager = models.ForeignKey(User, related_name='manager', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('PENDING', 'Pending'), ('APPROVED', 'Approved'), ('REVOKED', 'Revoked')], default='PENDING')

class Campaign(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    entries = models.ManyToManyField(AccessEntry)

# Create your models here.
