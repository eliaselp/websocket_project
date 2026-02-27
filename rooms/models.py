from django.db import models
import uuid
# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    master_token = models.CharField(max_length=100, default=uuid.uuid4, unique=True)
    slave_token = models.CharField(max_length=100, default=uuid.uuid4, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name