import typing
import os  # noqa
import threading  # noqa

from strawberry_django_plus import gql
from strawberry.types import Info

from chat_subscription.user.graphql.types import CustomUserType  # noqa
from chat_subscription.chat.graphql.types import RoomType, MessageType  # noqa
from chat_subscription.chat.models import Message, Room, RoomMember  # noqa
from chat_subscription.user.models import User  # noqa


@gql.type
class ChatSubscription:
    @gql.subscription
    async def yield_hello(self, info: Info) -> typing.AsyncGenerator[str, None]:
        ws = info.context.ws
        channel_layer = ws.channel_layer  # noqa
        async for message in ws.channel_listen("hello"):
            yield message["content"]

    @gql.subscription
    async def join_chat(
        self,
        info: Info,
        rooms: typing.List[gql.relay.GlobalID],
    ) -> typing.AsyncGenerator[MessageType, None]:
        user = User.objects.get(id=1)
        ws = info.context.ws
        channel_layer = ws.channel_layer
        room_ids = [f"room_{room.resolve_node(info)}" for room in rooms]
        for room in room_ids:
            # Join room group
            await channel_layer.group_add(room, ws.channel_name)
        for room in room_ids:
            await channel_layer.group_send(
                room,
                {
                    "type": "room.content",
                    "room_id": room,
                    "content": f"process: {os.getpid()} thread: {threading.current_thread().name}"
                    f" -> Hello my name is {user}!",
                },
            )
        async for message in ws.channel_listen("room.content", groups=room_ids):
            yield Message(
                room_id=message["room.id"],
                content=message["content"],
                sender=user,
            )
