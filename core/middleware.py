from urllib.parse import parse_qs
from channels.db import database_sync_to_async
import jwt
from django.conf import settings


@database_sync_to_async
def get_user_from_token(token):
    from django.contrib.auth.models import AnonymousUser
    from django.contrib.auth import get_user_model

    try:
        # Decode the token using the SECRET_KEY
        decoded_data = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        user_id = decoded_data.get("user_id")

        if user_id:
            return get_user_model().objects.get(id=user_id)
        else:
            return AnonymousUser()
    except (jwt.ExpiredSignatureError, jwt.DecodeError, get_user_model().DoesNotExist):
        return AnonymousUser()


class JWTAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        # Extract token from query string
        query_string = parse_qs(scope["query_string"].decode())
        token = query_string.get("token")

        if token:
            # Fetch user associated with this token asynchronously
            scope["user"] = await get_user_from_token(token[0])
        else:
            scope["user"] = AnonymousUser()

        # Call the inner application (the consumer)
        return await self.inner(scope, receive, send)
