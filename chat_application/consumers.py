import asyncio
import json
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from channels.consumer import AsyncConsumer
from . import models

class ChatConsumer():
    async def websocket_connect(self, event):
        print("connected", event)
        
        model_id = self.scope['url_route']['kwargs']['model_id']
        self.model_id = model_id
        self.model_room = model_id
        await self.channel_layer.group_add(
            self.model_room,
            self.channel_name
        )
        await self.send({
            "type": "websocket.accept"
        })

    async def websocket_receive(self, event):
        loaded_dict = json.loads(event.get('text', None))
        m = await self.save_chat(self.model_id, loaded_dict['user'], loaded_dict['message'])
        response = {
            'user': m.user,
            'message': m.message
        }
        await self.channel_layer.group_send(
            self.model_room,
            {
                "type": "chat_message",
                "text": json.dumps(response)
            }
        )

    async def chat_message(self, event):
        await self.send({
            "type": "websocket.send",
            "text": event['text']
        })

    async def websocket_disconnect(self, event):
        print("disconnected", event)

    @database_sync_to_async
    def save_chat(self, model_id, user, message):
        m = models.group.objects.get(i_id=model_id)
        return models.chats.objects.create(link=m, user=user, message=message)