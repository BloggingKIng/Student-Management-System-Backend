from django.db import models
import json
# Create your models here.

class SchoolInformation(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    description = models.TextField()
    props = models.TextField(blank=True) # serialized custom data

    @property
    def props_dict(self):
        return json.loads(self.props)
    def __str__(self):
        return self.name