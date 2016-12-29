from django import forms
from .models import User, Sentence

class AddUser(forms.Form):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class PostSentence(forms.Form):
	"""docstring for ClassName"""
	class Meta:
		model = Sentence
		fields = ('SID','Date','Content','Sentence_tag','Tpoic_tag','UID',)

