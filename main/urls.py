from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
        
    path("", views.index, name="index"),
    path("conversation/<str:pk>/", views.conversation, name="conversation"),

    path('create-conversation/', views.createConversation, name="create-conversation"),
    path('update-conversation/<str:pk>/', views.updateConversation, name="update-conversation"),
    path('delete-conversation/<str:pk>/', views.deleteConversation, name="delete-conversation"),

]