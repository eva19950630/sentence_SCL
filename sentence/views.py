from django.shortcuts import render
#google+
from .forms import AddUser, PostSentence
from .models import User, Sentence
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
# from django.utils import timezone
import datetime
# import pytz
# timezone.activate(pytz.timezone("Asia/Taipei"))

# Create your views here.

def index(request):
    return render(request, "sentence/index.html")

def sentence_post(request):
    if request.method == 'POST':
        django_form = PostSentence(request.POST)
        if django_form.is_valid():
            """ Assign data in Django Form to local variables """
            new_sentence = django_form.data.get("sentence")
            new_sentence_tag = django_form.data.get("language")
            get_uid = request.session['UID']
            # new_sid = str(len(Sentence.objects.all()) + 1)
            usermodel = User.objects.get(UID=get_uid)

            # current_tz = timezone.get_current_timezone()
            # createTime = current_tz.date()

            if User.objects.filter(UID = get_uid).exists():
                """ This is how your model connects to database and create a new member """
                Sentence.objects.create(
                    # SID = new_sid,
                    # Date = createTime,
                    Content = new_sentence,
                    Sentence_tag =  new_sentence_tag, 
                    UID = usermodel,
                )            
            return render(request, 'sentence/sentence.html')
            
        else:
            return render(request, 'sentence/index.html')
        
    else:
        return render(request, 'sentence/index.html')


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
    # print "hello world"
    if request.method == 'POST':
        
        django_form = AddUser(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            new_member_email = django_form.data.get("email")
            new_member_password= django_form.data.get('password')
            # new_uid = str(len(User.objects.all()) + 1)
           
            """ This is how your model connects to database and create a new member """
            User.objects.create(
                # UID = new_uid,
                UserName =  new_member_name, 
                Email = new_member_email,
                Password = new_member_password,
            )
                
            request.session['UID'] = User.objects.get(Email= new_member_email).UID
            return render(request, 'sentence/index.html',{'username': new_member_name})
            
        else:
            print('wrong form')
            return render(request, 'sentence/index.html',{'username': 'UserName'})
        
    else:
        return render(request, 'sentence/index.html')

#log in 
# def login_app(request):
#     if request.method == 'POST':
#         useremail = request.POST.get('email')
#         password = request.POST.get('password')

#         if User.objects.filter(Email=useremail, Password=password).exists():
#             print(login)
#             user = User.objects.filter(Email=useremail)[0]
#             username = user.UserName
#             print('login '+username)
#             return render(request, 'sentence/index.html') 
#     return render(request, 'sentence/index.html') 

def login_app(request):
    if User.objects.filter(Email=request.POST.get('email')).exists():
        m = User.objects.get(Email=request.POST.get('email'))
        if m.Password == request.POST.get('password'):
            request.session['UID'] = m.UID
            # print(m.UID)
            return render(request, 'sentence/index.html') 
        else:
            print('WRONG')
            return render(request, 'sentence/index.html')
    else:
        return render(request, 'sentence/index.html')            

#FB
def getuserid(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        userId = request.GET.get('userId')
        password = '000'
        # username = request.GET['username']
        # userId = request.GET['userId']
        # userpicture = request.GET['userpicture']
        # useremail = request.GET['useremail']
        # user_num = str(len(User.objects.all()) + 1)

        if User.objects.filter(SocialID = userId).exists():
            print('in session')
            request.session['UID'] = User.objects.get(UserName = username).UID
            # limit userId found to 0 object
            user = User.objects.filter(SocialID = userId)[0]
            # user.user_picture = userpicture
            user.save()
        else:
            print('create')
            User.objects.create(
                # UID = userId,
                UserName =  username,
                Password = password,
                SocialID = userId
                # Email = useremail
            )
        # print('fb login '+username)
        return render(request, "sentence/index.html",{'username': username})

#logout
def logout(request):
    print("logout")
    django_logout(request)
    return render(request, "sentence/index.html")

#google+
# def signup_google(request):
#     if request.method == 'POST':
    
#         user_form = AddUser(request.POST)
#         if user_form.is_valid():
        
#             new_user_id = user_form.data.get("uid")
#             new_user_name = user_form.data.get("username")
#             new_user_email = user_form.data.get("email")
            
            
#             User.objects.create(
#                 uid = new_user_id,
#                 username = new_user_name,
#                 email = new_user_email,
#             )
            
#             return render(request, 'sentence/index.html')
        
#         else:
#             return render(request, 'sentence/index.html')
        
#     else:
#         return render(request, 'sentence/index.html')