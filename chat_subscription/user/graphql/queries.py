import strawberry

from gqlauth.user.queries import UserQueries
from .types import CustomUserType  # noqa
from strawberry.types import Info

@strawberry.type
class UserQuery(UserQueries):
    @strawberry.field
    async def users(self, info: Info) -> str:
        #x = info.context.request.scope.get("user")
        #print(x)
        user = info.context.user
        
        return user
    ...
