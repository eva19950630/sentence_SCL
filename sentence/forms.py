from django import forms
from .models import User, Sentence ,Translation

class AddUser(forms.Form):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class PostSentence(forms.Form):
	"""docstring for ClassName"""
	class Meta:
		model = Sentence
		fields = ('Content','Sentence_tag','Tpoic_tag','UID','Link',)


class PostTranslate(forms.Form):
	"""docstring for ClassName"""
	class Meta:
		model = Translation
		fields = ('Content','SID','UID','Translation_tag',)

