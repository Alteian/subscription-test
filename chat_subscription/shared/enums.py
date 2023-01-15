from django.db import models


class MessageStatus(models.TextChoices):
    READ = "READ", "Read"
    UNREAD = "UNREAD", "Unread"
