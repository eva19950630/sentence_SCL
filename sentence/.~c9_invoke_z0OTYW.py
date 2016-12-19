from django.shortcuts import render
#google+
from .forms import AddUser
from .models import User
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
	return render(request, "sentence/index.html")

def sentence(request):
	return render(request, "sentence/sentence.html")

def sentence_world(request):
	return render(request, "sentence/sentence_world.html")

def post_world(request):
	return render(request, "sentence/post_world.html")

def usermap(request):
	return render(request, "sentence/usermap.html")

def user_profile(request):
	return render(request, "sentence/user_profile.html")

def user_account(request):
	return render(request, "sentence/user_account.html")

def user_achievement(request):
	return render(request, "sentence/user_achievement.html")

def user_history(request):
	return render(request, "sentence/user_history.html")

#app signup
def signup_app(request):
    if request.method == 'POST':
        
        django_form = AddUser(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            new_member_email = django_form.data.get("email")
            new_member_password= django_form.data.get('password')
            
            """ This is how your model connects to database and create a new member """
            User.objects.create(
                name =  new_member_name, 
                email = new_member_email,
                password = new_member_password,
                )

#google+
def signup_google(request):
    if request.method == 'POST':
    
        user_form = AddUser(request.POST)
        if user_form.is_valid():
        
            new_user_id = user_form.data.get("uid")
            new_user_name = user_form.data.get("username")
            new_user_email = user_form.data.get("email")
            
            
            User.objects.create(
                uid = new_user_id,
                username = new_user_name,
                email = new_user_email,
            )
            
            return render(request, 'sentence/index.html')
        
        else:
            return render(request, 'sentence/index.html')
        
    else:
        return render(request, 'sentence/index.html')