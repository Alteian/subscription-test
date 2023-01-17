import typing
import os  # noqa
import threading  # noqa
import asyncio
import strawberry

from strawberry_django_plus import gql
from strawberry.types import Info

from chat_subscription.user.graphql.types import CustomUserType  # noqa
from chat_subscription.chat.graphql.types import RoomType, MessageType  # noqa
from chat_subscription.chat.graphql.inputs import RoomInput  # noqa
from chat_subscription.chat.models import Message, Room, RoomMember  # noqa
from chat_subscription.user.models import User  # noqa


@strawberry.type
class ChatSubscription:
    @strawberry.subscription
    def chat(
        self,
        info: Info,
        rooms: list[RoomInput],
        ) -> typing.AsyncGenerator[MessageType, None]:


        ...


    @strawberry.mutation
    async def send_chat_message(
        self,
        info: Info,
        room: gql.relay.GlobalID,
        content: str,
        ) -> None:
        ws = info.context.ws
        channel_layer = ws.channel_layer
        Message.objects.create(room=room.resolve_node(info), content=content)
        await channel_layer.group_send(
            f"chat_{room.resolve_node(info)}",
            {
                "type": "room.message",
                "room_id": room.id,
                "content": content,
            },
        )
    
    @strawberry.mutation
    async def create_room(
        self,
        info: Info,
        ) -> RoomType:
        ws = info.context.ws
        channel_layer = ws.channel_layer
        #user = info.context.scope.get("user")
        room = Room.objects.create()
        #RoomMember.objects.create(user=user, room=room)
        return room
