import strawberry

from strawberry.types import Info

from chat_subscription.chat.graphql.types import RoomType
from chat_subscription.chat.models import Room, RoomMember
from strawberry_django_plus import gql


@strawberry.type
class ChatMutation:
    @strawberry.mutation
    async def send_chat_message(
        self,
        info: Info,
        room: gql.relay.GlobalID,
        content: str,
    ) -> None:
        ws = info.context.ws
        channel_layer = ws.channel_layer

        await channel_layer.group_send(
            f"chat_{room.resolve_node(info)}",
            {
                "type": "room.message",
                "room_id": room.id,
                "content": content,
            },
        )

    @strawberry.mutation
    def create_room(
        self,
        info: Info,
    ) -> RoomType:
        user = info.context.request.user
        room = Room.objects.create()
        RoomMember.objects.create(user=user, room=room)
        return room
