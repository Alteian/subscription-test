"""chat_subscription URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from strawberry.django.views import GraphQLView
from strawberry.http import GraphQLHTTPResponse
from strawberry.types import ExecutionResult

from graphql.error.graphql_error import format_error as format_graphql_error
from django.http import HttpRequest, HttpResponse
from strawberry.django.context import StrawberryDjangoContext
from typing import Any
from .schema import schema


class CustomGraphQLView(GraphQLView):
    def get_context(self, request: HttpRequest, response: HttpResponse) -> Any:
        return StrawberryDjangoContext(request=request, response=response)

    def process_result(self, request: HttpRequest, result: ExecutionResult) -> GraphQLHTTPResponse:
        data: GraphQLHTTPResponse = {"data": result.data}

        if result.errors:
            data["errors"] = [format_graphql_error(err) for err in result.errors]

        return data


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "graphql/",
        CustomGraphQLView.as_view(
            graphiql=True,
            schema=schema,
        ),
    ),
]
