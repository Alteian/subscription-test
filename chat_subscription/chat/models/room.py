from django.db import models

from chat_subscription.shared.models.base_model import BaseModel


class Room(BaseModel):
    is_active = models.BooleanField(default=True)
    is_private = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]
