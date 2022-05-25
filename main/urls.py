from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("conversation/<str:pk>/", views.conversation, name="conversation"),

path('create-conversation/', views.createConversation, name="create-conversation"),
]