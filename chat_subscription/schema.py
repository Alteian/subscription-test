from strawberry import Schema
from strawberry.tools import merge_types  # noqa
from strawberry.schema.config import StrawberryConfig
from strawberry.extensions import QueryDepthLimiter
from strawberry_django_plus.directives import SchemaDirectiveExtension
from strawberry_django_plus.optimizer import DjangoOptimizerExtension

# import chat_subscription.chat.graphql.schema
# import chat_subscription.user.graphql.schema
from chat_subscription.user.graphql.schema import Query, Mutation


# Mutation = merge_types()
# Query = merge_types()
# @strawberry.type
# class Query:
#    @strawberry.field(description="A simple ping to test the server.")
#    def ping(self) -> str:
#        return "pong"


schema = Schema(
    query=Query,
    mutation=Mutation,
    config=StrawberryConfig(
        auto_camel_case=True,
    ),
    extensions=[
        QueryDepthLimiter(max_depth=10),  # TODO: find optimal amount.
        SchemaDirectiveExtension,
        DjangoOptimizerExtension,
    ],
)
