from django import forms
from .models import User, Sentence, Translation, Topic

class AddUser(forms.Form):
    
    class Meta:
        model = User

        fields = ('username', 'email', 'password','UserIcon','language',)

        def clean_email(self):
		    email = self.cleaned_data['email']
		    if User.objects.filter(Email=email).exists():
		        raise forms.ValidationError("Email already exists")
		    return email

		# def clean(self):
		#     form_data = self.cleaned_data
		#     if form_data['password'] != form_data['password_repeat']:
		#     	self._errors["password"] = ["Password do not match"] # Will raise a error message
		#         del form_data['password']
		#     return form_data


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

