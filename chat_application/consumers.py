import asyncio
import json
from django.contrib.auth import get_user_model
from channels.db import database_sync_to_async
from channels.consumer import AsyncConsumer


class ChatConsumer():
    pass