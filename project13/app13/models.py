from django.db import models

# Create your models here.
class User(models.Model):
    DISABILITY_CHOICES = [
        ('dum', 'Dumb'),
        ('duff', 'Deaf'),
    ]

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    disability = models.CharField(max_length=10, choices=DISABILITY_CHOICES)

    def __str__(self):
        return self.username
