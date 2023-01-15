from django.db import models
from strawberry_django_plus import gql


@gql.enum
class MessageStatus(models.TextChoices):
    READ = "READ", "Read"
    UNREAD = "UNREAD", "Unread"
