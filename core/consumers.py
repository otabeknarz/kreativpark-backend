import json

from channels.generic.websocket import AsyncWebsocketConsumer


class SeatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'sections_group'
        self.user = self.scope['user']

        if not self.user.is_authenticated:
            await self.accept()
            await self.send(text_data=json.dumps({
                'message': 'You are not authenticated',
            }))
            await self.close()
            return

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        await self.send(text_data=json.dumps({
            'message': 'You are connected',
            'user': self.user.username,
        }))

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        await self.close()

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        seat_id = text_data_json['seat_id']
        status = text_data_json['status']

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'seat_id': seat_id,
                'user': self.user.username,
                'status': status,
            }
        )

    async def chat_message(self, event):
        seat_id = event['seat_id']
        status = event['status']

        await self.send(text_data=json.dumps({
            'seat_id': seat_id,
            'user': self.user.username,
            'status': status,
        }))
