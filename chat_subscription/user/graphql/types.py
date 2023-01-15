import typing  # noqa

from strawberry_django_plus import gql

from chat_subscription.user.models import User


@gql.django.type(User)
class CustomUserType:
    email: gql.auto
    username: gql.auto
    date_joined: gql.auto
