import re
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Conversation, Topic
from .forms import ConversationForm
# Create your views here.

# conversations = [
#     {'id':1, 'name': 'Mark'},
#     {'id':2, 'name': 'Jim'},
#     {'id':3, 'name': 'Sally'},
# ]

def loginPage(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('index')


def index(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    conversations = Conversation.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
        )

    topics = Topic.objects.all() 
    conversation_count = conversations.count()
    
    context = {'conversations': conversations, 'topics': topics, 'conversation_count': conversation_count}
    return render(request, 'base/home.html', context)

def conversation(request, pk): 
    conversation = Conversation.objects.get(id=pk)
    # for i in conversations:
    #     if i['id'] == int(pk):
    #         conversation = i
    context = {'conversation': conversation}
    return render(request, 'base/conversation.html', context)

@login_required(login_url='/login')
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


