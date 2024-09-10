import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': "You're connected to chat websocket"
        }))

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('Message from client: ', message)
        #
        #self.send(text_data=json.dumps({
        #    'type': 'chat',
        #    'message': message
        #}))

    def disconnect(self, code):
        pass


class ChatRoomConsumer(WebsocketConsumer):

    def connect(self):
        self.group_name = 'chat'
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()
        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': "You're connected to websocket"
        }))

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print('Message from client: ', message)
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({
            'type': 'chat',
            'message': message
        }))

class UserOnlineNotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.group_name = 'user_online_notification'
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name, self.channel_name
        )

    def user_online(self, event):
        print('user_online()', event)
        self.send(text_data=event['message'])