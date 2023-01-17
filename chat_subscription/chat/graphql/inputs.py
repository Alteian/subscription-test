import strawberry

from strawberry_django_plus import gql

@strawberry.input
class RoomInput:
    id: gql.relay.GlobalID
