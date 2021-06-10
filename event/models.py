from django.db import models
from user.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Event(models.Model):
    host_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.URLField()
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=300)
    is_private = models.BooleanField()
    start_dttime = models.DateTimeField()
    end_dttime = models.DateTimeField()
    capacity = models.IntegerField()
    attending_user = ArrayField(models.IntegerField(), blank=True, default=list)



