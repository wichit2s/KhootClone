from django.urls import path
from quiz.views import *

urlpatterns = [
    path('', home),
    path('create/', create),
    path('json/', json),
    path('pdf/', pdf),
    path('bg/', bg),
    path('blurbg/', blurbg),
]
