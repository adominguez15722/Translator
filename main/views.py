from django.shortcuts import render

# Create your views here.

conversations = [
    {'id':1, 'name': 'Mark'},
    {'id':2, 'name': 'Jim'},
    {'id':3, 'name': 'Sally'},
]

def index(response): 
    return render(response, 'home.html', {'conversations': conversations})

def conversation(response): 
    return render(response, 'conversation.html')
