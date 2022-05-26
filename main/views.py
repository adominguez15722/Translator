from django.shortcuts import render, redirect
from .models import Conversation
from .forms import ConversationForm
# Create your views here.

# conversations = [
#     {'id':1, 'name': 'Mark'},
#     {'id':2, 'name': 'Jim'},
#     {'id':3, 'name': 'Sally'},
# ]

def index(response):
    conversations = Conversation.objects.all() 
    context = {'conversations': conversations}
    return render(response, 'base/home.html', context)

def conversation(response, pk): 
    conversation = Conversation.objects.get(id=pk)
    # for i in conversations:
    #     if i['id'] == int(pk):
    #         conversation = i
    context = {'conversation': conversation}
    return render(response, 'base/conversation.html', context)

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


