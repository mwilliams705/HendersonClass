from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    school_id = models.IntegerField()
    school_email = models.EmailField()
    is_teacher = models.BooleanField()