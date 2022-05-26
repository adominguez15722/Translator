from django.forms import ModelForm
from .models import Conversation

class ConversationForm(ModelForm):
    class Meta:
        model = Conversation
        fields = '__all__'
        