from django.shortcuts import render
from .models import Conversation
# Create your views here.

# conversations = [
#     {'id':1, 'name': 'Mark'},
#     {'id':2, 'name': 'Jim'},
#     {'id':3, 'name': 'Sally'},
# ]

def index(response):
    conversations = Conversation.objects.all() 
    context = {'conversations': conversations}
    return render(response, 'main/home.html', context)

def conversation(response, pk): 
    conversation = Conversation.objects.get(id=pk)
    # for i in conversations:
    #     if i['id'] == int(pk):
    #         conversation = i
    context = {'conversation': conversation}
    return render(response, 'main/conversation.html', context)

def createConversation(request):
    context = {}
    return render(request, 'main/conversation_form.html', context)

