from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    description = models.TextField(max_length=50)
    autor = models.CharField(max_length=30, null=True)
  
    is_activate = models.BooleanField(default=True)

    class Meta:
        db_table = 'blogs'