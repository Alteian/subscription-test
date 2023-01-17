import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import re_path, path  # noqa
from strawberry.channels import GraphQLHTTPConsumer, GraphQLWSConsumer
from django.conf import settings  # noqa


os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)
django_asgi_app = get_asgi_application()


from .schema import schema  # noqa
class DebuggableGraphQLWSConsumer(GraphQLWSConsumer):
    async def get_context(self, *args, **kwargs) -> object:
        context = await super().get_context(*args, **kwargs)
        #context = await self._handler.get_context(*args, **kwargs)
        context.tasks = self._handler.tasks
        
        return context


class DebuggableGraphQLHTTPConsumer(GraphQLHTTPConsumer):
    async def get_context(self, *args, **kwargs) -> object:
        context = await super().get_context(*args, **kwargs)
        context.user = "test"
        return context


websocket_urlpatterns = [
    re_path("^ws/graphql/", DebuggableGraphQLWSConsumer.as_asgi(schema=schema)),
]

gql_http_consumer = AuthMiddlewareStack(DebuggableGraphQLHTTPConsumer.as_asgi(schema=schema))
gql_ws_consumer = DebuggableGraphQLWSConsumer.as_asgi(schema=schema)

application = ProtocolTypeRouter(
    {
        "http": URLRouter(
            [
                re_path("^ws/graphql/", gql_http_consumer),
                re_path("^", django_asgi_app),
            ]
        ),
        "websocket": URLRouter(websocket_urlpatterns),
    }
)
"""
ASGI config for chat_subscription project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
"""
import os

from django.core.asgi import get_asgi_application
from strawberry.channels import GraphQLProtocolTypeRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chat_subscription.settings")

django_asgi_app = get_asgi_application()
from .schema import schema
application = GraphQLProtocolTypeRouter(
    schema,
    django_application=django_asgi_app,
)"""
