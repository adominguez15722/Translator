import re
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Conversation, Topic
from .forms import ConversationForm
# Create your views here.

# conversations = [
#     {'id':1, 'name': 'Mark'},
#     {'id':2, 'name': 'Jim'},
#     {'id':3, 'name': 'Sally'},
# ]

def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    conversations = Conversation.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    topics = Topic.objects.all() 
    
    context = {'conversations': conversations, 'topics': topics}
    return render(request, 'base/home.html', context)

def conversation(request, pk): 
    conversation = Conversation.objects.get(id=pk)
    # for i in conversations:
    #     if i['id'] == int(pk):
    #         conversation = i
    context = {'conversation': conversation}
    return render(request, 'base/conversation.html', context)

def createConversation(request):
    form = ConversationForm()
    if request.method == 'POST':
        form = ConversationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'base/conversation_form.html', context)



def updateConversation(request, pk):
    conversation = Conversation.objects.get(id=pk)
    form = ConversationForm(instance=conversation)

    if request.method == 'POST':
        form = ConversationForm(request.POST, instance=conversation)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'base/conversation_form.html', context)

def deleteConversation(request, pk):
    conversation = Conversation.objects.get(id=pk)
    if request.method == 'POST':
        conversation.delete()
        return redirect('index')
    return render(request, 'base/delete.html', {'obj':conversation})


