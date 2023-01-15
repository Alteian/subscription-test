from django.db import models

from chat_subscription.shared.models.base_model import BaseModel


class RoomMember(BaseModel):
    room = models.ForeignKey(
        "chat.Room",
        on_delete=models.CASCADE,
        related_name="members",
    )
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="rooms")
