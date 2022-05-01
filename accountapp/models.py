from django.db import models

# Create your models here.
# Like SQL files to create table

class HelloWorld(models.Model):
    # null = false : must be
    text = models.CharField(max_length=255, null=False)