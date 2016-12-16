from django.shortcuts import render

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