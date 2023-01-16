from strawberry import Schema
from strawberry.tools import merge_types  # noqa
from strawberry.schema.config import StrawberryConfig
from strawberry.extensions import QueryDepthLimiter
from strawberry_django_plus.directives import SchemaDirectiveExtension
from strawberry_django_plus.optimizer import DjangoOptimizerExtension

import chat_subscription.chat.graphql.schema
import chat_subscription.user.graphql.schema

Mutation = merge_types(
    name="Mutation",
    types=(
        chat_subscription.chat.graphql.schema.ChatMutation,
        chat_subscription.user.graphql.schema.UserMutation,
    ),
)
Query = chat_subscription.user.graphql.schema.UserQuery
Subscription = chat_subscription.chat.graphql.schema.ChatSubscription
# @strawberry.type
# class Query:
#    @strawberry.field(description="A simple ping to test the server.")
#    def ping(self) -> str:
#        return "pong"


schema = Schema(
    query=Query,
    mutation=Mutation,
    subscription=Subscription,
    config=StrawberryConfig(
        auto_camel_case=True,
    ),
    extensions=[
        QueryDepthLimiter(max_depth=10),
        SchemaDirectiveExtension,
        DjangoOptimizerExtension,
    ],
)
