import typing  # noqa

from strawberry_django_plus import gql

from chat_subscription.chat.models import Message, Room, RoomMember  # noqa

from chat_subscription.user.graphql.types import CustomUserType


@gql.django.type(Room)
class RoomType(gql.relay.Node):
    messages: gql.relay.Connection["MessageType"]
    is_active: gql.auto
    is_private: gql.auto


@gql.django.type(Message)
class MessageType(gql.relay.Node):
    room: RoomType
    sender: CustomUserType
    content: gql.auto
    status: gql.auto
