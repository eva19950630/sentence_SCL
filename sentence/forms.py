from django import forms
from .models import User, Sentence, Translation, Topic, Friendship

class AddUser(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'email', 'password','UserIcon','NativeLanguage')

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

class AddFriend(forms.Form):
	"""docstring for ClassName"""
	class Meta:
		model = Friendship
		fields = ('Friend','UID',)

class ImageUploadForm(forms.ModelForm):
    """Image upload form."""
    class Meta:
    	model = User
    	fields = ('UserIcon','NativeLanguage')


# """ valid login """
# class AuthenticationForm(forms.Form):
#     """
#     Base class for authenticating users. Extend this to get a form that accepts
#     username/password logins.
#     """
#     username = forms.CharField( max_length=30)
#     password = forms.CharField(widget=forms.PasswordInput)

#     def __init__(self, request=None, *args, **kwargs):
#         """
#         If request is passed in, the form will validate that cookies are
#         enabled. Note that the request (a HttpRequest object) must have set a
#         cookie with the key TEST_COOKIE_NAME and value TEST_COOKIE_VALUE before
#         running this validation.
#         """
#         self.request = request
#         self.user_cache = None
#         super(AuthenticationForm, self).__init__(*args, **kwargs)

#     def clean(self):
#         username = self.cleaned_data.get('username')
#         password = self.cleaned_data.get('password')

#         if username and password:
#             self.user_cache = authenticate(username=username, password=password)
#             if self.user_cache is None:
#                 raise forms.ValidationError(_("Please enter a correct username and password. Note that both fields are case-sensitive."))
#             elif not self.user_cache.is_active:
#                 raise forms.ValidationError(_("This account is inactive."))

#         # TODO: determine whether this should move to its own method.
#         if self.request:
#             if not self.request.session.test_cookie_worked():
#                 raise forms.ValidationError(_("Your Web browser doesn't appear to have cookies enabled. Cookies are required for logging in."))

#         return self.cleaned_data

#     def get_user_id(self):
#         if self.user_cache:
#             return self.user_cache.id
#         return None

#     def get_user(self):
#         return self.user_cache

#     def clean_username(self):
# 	    username = self.cleaned_data['username']
# 	    try:
# 	        User.objects.get(username=username)
# 	    except User.DoesNotExist:
# 	        raise forms.ValidationError("The username you have entered does not exist.")
# 	    return username