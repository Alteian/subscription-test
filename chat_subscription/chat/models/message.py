from django.db import models

from chat_subscription.shared.models.base_model import BaseModel
from chat_subscription.shared.enums import MessageStatus
from chat_subscription.user.models.user import User


class Message(BaseModel):
    room = models.ForeignKey(
        "chat.Room",
        on_delete=models.CASCADE,
        related_name="messages",
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    status = models.CharField(choices=MessageStatus.choices, default=MessageStatus.UNREAD, max_length=10)

    class Meta:
        ordering = ["-created"]
