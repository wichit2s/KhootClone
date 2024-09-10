from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in, sender=User)
def send_user_online_notification(sender, request, user, **kwargs):
    print('signals user_logged_in', user.username)
    channel_layer = get_channel_layer()
    group_name = 'user_online_notification'
    event = {
        'type': 'user_online',
        'message': user.username,
    }
    async_to_sync(channel_layer.group_send)(group_name, event)
    print(user.username, 'user online notification sent')
