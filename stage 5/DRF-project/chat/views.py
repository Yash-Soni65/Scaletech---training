from django.shortcuts import render

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        await self.accept()

    async def receive(self, text_data):

        print(text_data)

    async def disconnect(self, close_code):

        pass

# Create your views here.
