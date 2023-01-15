import typing

from strawberry_django_plus import gql

from chat_subscription.user.graphql.types import CustomUserType


@gql.type
class Subscription:
    @gql.subscription
    async def join_chat(self, info, chat_id: int) -> typing.Optional[typing.List[CustomUserType]]:
        user = info.context.request.user

        return user
