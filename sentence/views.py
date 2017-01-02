from django.shortcuts import render
#google+
from .forms import AddUser, PostSentence, PostTranslate, PostTopic
from .models import User, Sentence, Translation, Topic
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
# from django.utils import timezone
import datetime
from django.core.urlresolvers import reverse
# import pytz
# timezone.activate(pytz.timezone("Asia/Taipei"))

# Create your views here.

def index(request): 
    if request.session.get('UID'):
        usermodel = User.objects.get(UID=request.session['UID'])
        return render(request, "sentence/index.html",{'username': usermodel})
    else:
        return render(request, "sentence/index.html")

# def show_link(request, obj):

def sentence_url(request, sid):
    # print('sentence_url called')
    if request.session.get('UID'):
        usermodel = User.objects.get(UID=request.session['UID'])
        new_sentence = Sentence.objects.get(SID = int(sid))
        return render(request, 'sentence/sentence.html',{'sentence_content': new_sentence,'username': usermodel})
    else:
        new_sentence = Sentence.objects.get(SID = int(sid))
        return render(request, 'sentence/sentence.html',{'sentence_content': new_sentence})

def sentence_post(request):
    # print('sentence_post called')
    # print(sid)
    if request.method == 'POST':
        django_form = PostSentence(request.POST)
        get_uid = request.session.get('UID')
        usermodel = User.objects.get(UID=get_uid)

        if django_form.is_valid():
            if django_form.data.get("topic"):
                new_sentence = django_form.data.get("sentence")
                new_sentence_tag ='#' + django_form.data.get("language")
                new_sentence_topic ='#' + django_form.data.get("topic")
                new_sentence_link = django_form.data.get("link")

                if User.objects.filter(UID = get_uid).exists():
                    """ This is how your model connects to database and create a new member """

                    new_topic_model = Topic.objects.create(
                        Topic_tag = new_sentence_topic,
                        Link = new_sentence_link,
                    ) 

                    new_sentence_model = Sentence.objects.create(
                        Content = new_sentence,
                        Sentence_tag =  new_sentence_tag, 
                        UID = usermodel,
                        TopicID = new_topic_model,
                    )           

                print("topic sentence  store")
                return HttpResponseRedirect(reverse('sentence_url',kwargs={'sid': new_sentence_model.SID}))
                # return render(request, 'sentence/sentence.html')
            else:       
                """ daily sentence """
                new_sentence = django_form.data.get("sentence")
                new_sentence_tag = '#' + django_form.data.get("language")

                if User.objects.filter(UID = get_uid).exists():
                    """ This is how your model connects to database and create a new member """
                    new_sentence_model = Sentence.objects.create(
                        Content = new_sentence,
                        Sentence_tag =  new_sentence_tag, 
                        UID = usermodel,
                    )            
                print("daily sentence  store " + str(new_sentence_model.SID))
                # return Redirect(reverse('sentence_url',kwargs={'sid': new_sentence_model.SID}))
                return HttpResponseRedirect(reverse('sentence_url',kwargs={'sid': new_sentence_model.SID}))
                # return render(request, 'sentence/sentence.html',{'sentence_content': new_sentence})                     
        else:
            return render(request, 'sentence/index.html')
        
    else:
        return render(request, 'sentence/index.html')


def translation_post(request, get_sid):
    # print('get_sid '+get_sid)
    if request.method == 'POST':
        django_form = PostTranslate(request.POST)
        if django_form.is_valid():
                
                sentencemodel = Sentence.objects.get(SID = int(get_sid))
                new_translation = django_form.data.get("translation")
                new_translation_tag = '#' + django_form.data.get("translation_tag")
                
                # link

                get_uid = request.session.get('UID')
                usermodel = User.objects.get(UID=get_uid)

                #get sid

                if User.objects.filter(UID = get_uid).exists():
                    """ This is how your model connects to database and create a new member """
                    new_translation_model = Translation.objects.create(
                        Content = new_translation,
                        Translation_tag =  new_translation_tag, 
                        UID = usermodel,
                        SID =sentencemodel,
                    )            
                print("translation store")
                return HttpResponseRedirect(reverse('sentence_url',kwargs={'sid': get_sid}))
                # return render(request, "sentence/sentence.html",{'translation_model': new_translation_model,'username': usermodel})                    
        else:
            return render(request, 'sentence/index.html')
        
    else:
        return render(request, 'sentence/index.html')

def sentence(request):
    return render(request, "sentence/sentence.html")
       
def sentence_world(request):
	return render(request, "sentence/sentence_world.html")

def post_world(request):
    # print('post_world called')
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
    get_uid = request.session.get('UID')
    sentencemodel = Sentence.objects.filter(UID=get_uid)
    translationmodel = Translation.objects.filter(UID=get_uid)
    return render(request, "sentence/user_history.html",{'sentence_model': sentencemodel,'translation_model': translationmodel})



def login_app(request):
    if User.objects.filter(Email=request.POST.get('email')).exists():
        m = User.objects.get(Email=request.POST.get('email'))
        if m.Password == request.POST.get('password'):
            request.session['UID'] = m.UID
            print(m.UserName)
            return render(request, 'sentence/index.html',{'username': m}) 
        else:
            print('Password WRONG')
            return render(request, 'sentence/index.html')
    else:
        print('NOT USER')
        django_form = AddUser(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            new_member_email = django_form.data.get("email")
            new_member_password= django_form.data.get('password')
            # new_uid = str(len(User.objects.all()) + 1)
           
            """ This is how your model connects to database and create a new member """
            new_user_model=User.objects.create(
                # UID = new_uid,
                UserName =  new_member_name, 
                Email = new_member_email,
                Password = new_member_password,
            )
                
            request.session['UID'] = new_user_model.UID
            return render(request, 'sentence/index.html',{'username': new_user_model})
            
        else:
            print('wrong form')
            return render(request, 'sentence/index.html')
        return render(request, 'sentence/index.html')            

#FB
def getuserid(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        userId = request.GET.get('userId')
        password = '000'
        if User.objects.filter(SocialID = userId).exists():
            # print('in session')
            request.session['UID'] = User.objects.get(UserName = username).UID
            # limit userId found to 0 object
            user = User.objects.filter(SocialID = userId)[0]
            # user.user_picture = userpicture
            user.save()
        else:
            print('create')
            new_user_model = User.objects.create(
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