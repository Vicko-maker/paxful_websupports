from django.db import models


# Create your models here.
class Person(models.Model):
    email = models.EmailField(max_length=50)
    username = models.CharField(max_length=100)

    def __unicode__(self):
        return self.email
