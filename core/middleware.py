from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from channels.middleware import BaseMiddleware
from jwt import decode as jwt_decode, ExpiredSignatureError, InvalidTokenError
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


@database_sync_to_async
def get_user_from_jwt(token):
    try:
        decoded_data = jwt_decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_data.get("user_id")

        return User.objects.get(id=user_id)
    except (ExpiredSignatureError, InvalidTokenError, User.DoesNotExist):
        return AnonymousUser()


class JWTAuthMiddleware(BaseMiddleware):
    async def __call__(self, scope, receive, send):
        headers = dict(scope['headers'])
        token = None

        if b'sec-websocket-protocol' in headers:
            protocols = headers[b'sec-websocket-protocol'].decode().split(',')
            token = protocols[0].strip()

        scope['user'] = await get_user_from_jwt(token)
        return await super().__call__(scope, receive, send)
