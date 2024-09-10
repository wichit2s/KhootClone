from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req, 'chat/home.html')

def notification(req):
    return render(req, 'chat/notification.html')
