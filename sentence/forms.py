from django import forms
from .models import User, Sentence, Translation, Topic

class AddUser(forms.Form):
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class PostSentence(forms.Form):
	"""docstring for ClassName"""
	class Meta:
		model = Sentence
		fields = ('Content','Sentence_tag','UID',)


class PostTranslate(forms.Form):
	"""docstring for ClassName"""
	class Meta:
		model = Translation
		fields = ('Content','SID','UID','Translation_tag',)

class PostTopic(forms.Form):
	"""docstring for ClassName"""
	class Meta:
		model = Topic
		fields = ('Topic_tag','Link',)

