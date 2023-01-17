import strawberry

from strawberry.types import Info

# from chat_subscription.chat.graphql.types import RoomType
from chat_subscription.chat.models import Room, RoomMember
from strawberry_django_plus import gql
from chat_subscription.chat.graphql.subscriptions import RoomType

@strawberry.type
class ChatMutation:
    ...

    