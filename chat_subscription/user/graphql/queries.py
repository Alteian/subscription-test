import strawberry

from gqlauth.user.queries import UserQueries
from .types import CustomUserType  # noqa


@strawberry.type
class UserQuery(UserQueries):
    ...
