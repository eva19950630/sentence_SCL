from django.shortcuts import render
#google+
from .forms import AddUser, PostSentence, PostTranslate, PostTopic
from .models import User, Sentence, Translation, Topic, Country, Country_language, Language, Collection
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
# from django.utils import timezone
import datetime
from django.core.urlresolvers import reverse
#json by Gim
from django.http import JsonResponse
from django.http import HttpResponse
import json
# import pytz
# timezone.activate(pytz.timezone("Asia/Taipei"))

# Create your views here.

def index(request): 
    sentencemodel_date_order = Sentence.objects.filter().order_by('-Date')[:12]
    sentencemodel_like_order = Sentence.objects.filter().order_by('-Likes')[:12]

    uid = request.session.get('UID')

    if User.objects.filter(UID = uid).exists():
        if request.session.get('UID'):
            print('login index')
            # try:
            #     usermodel = User.objects.get(UID=request.session['UID'])
            # except User.DoesNotExist:
            #     usermodel = None
            # return render(request, "sentence/index_afterlogin.html",{'username': usermodel,'sentence_content': sentencemodel})
            
            usermodel = User.objects.get(UID=request.session['UID'])

            context = {'username': usermodel,'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,'extend_index': 'sentence/background.html'}

            return render(request, "sentence/index_afterlogin.html",context)
        
        else:
            print('logout index')
            context = {'sentence_content': sentencemodel_like_order,'sentence_content_date': sentencemodel_date_order
            ,'extend_index': 'sentence/background.html'}
            return render(request, "sentence/index.html",context)
    else:
        context = {'sentence_content': sentencemodel_like_order,'sentence_content_date': sentencemodel_date_order
        ,'extend_index': 'sentence/background.html'}
        return render(request, "sentence/index.html",context)

# def show_link(request, obj):

def sentence_url(request, sid):
    # print('sentence_url called')
    sentencemodel = Sentence.objects.get(SID = int(sid))

    #views count
    views = sentencemodel.Views
    viewed = False
    # if request.session.get('has_viewed_'+str(sid), liked):
    #     liked = True
    if request.session.get('has_viewed_'+str(sid),viewed):
        print('has view')
    else:
        print('view')
        request.session['has_viewed_'+str(sid)] = True
        views = views + 1
        sentencemodel.Views = views
        sentencemodel.save()    

    if request.session.get('UID'):
        # usermodel = User.objects.get(UID=request.session.get('UID'))
        # try:
        #     usermodel = User.objects.get(UID=request.session['UID'])
        # except User.DoesNotExist:
        #     usermodel = None
        # # new_sentence = Sentence.objects.get(SID = int(sid))
        # return render(request, 'sentence/sentence.html',{'sentence_content': new_sentence,'username': usermodel})
        collectionmodel = Collection.objects.filter(UID=request.session.get('UID'),SID=sid)
        usermodel = User.objects.get(UID=request.session.get('UID'))
        liked = False
        if request.session.get('has_liked_'+str(sid), liked):
            liked = True
            print("liked {}_{}".format(liked, sid))

        isCollect = 'Collect'
        if Collection.objects.filter(UID=usermodel.UID,SID=sid).exists():
            isCollect = 'UnCollected'

        if collectionmodel:
            context = {'sentence_content': sentencemodel,'username': usermodel,
            'liked': liked,'extend_index': 'sentence/background.html','collected': isCollect,
            'collect':collectionmodel}
        else:
            context = {'sentence_content': sentencemodel,'username': usermodel,
            'liked': liked,'extend_index': 'sentence/background.html','collected': isCollect}

        return render(request, 'sentence/sentence.html',context)
    else:
        context = {'sentence_content': sentencemodel,'extend_index': 'sentence/background.html'}
        return render(request, 'sentence/sentence.html',context)

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
                    #if topic exist
                    if(Topic.objects.filter(Topic_tag=new_sentence_topic).exists()):
                        new_topic_model = Topic.objects.get(Topic_tag=new_sentence_topic)

                        new_sentence_model = Sentence.objects.create(
                            Content = new_sentence,
                            Sentence_tag =  new_sentence_tag, 
                            UID = usermodel,
                            TopicID = new_topic_model,
                        )           
                    else:
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

# def sentence(request):
#     return render(request, "sentence/sentence.html")
       
# def sentence_world(request):
# 	return render(request, "sentence/sentence_world.html")

# def post_world(request):
#     # print('post_world called')
#     return render(request, "sentence/post_world.html")

def usermap(request):
    if request.session.get('UID'):
        usermodel = User.objects.get(UID=request.session.get('UID'))

        context = {'username': usermodel,'extend_index': 'sentence/background.html'}

        return render(request, "sentence/usermap.html",context)
    else:
        context = {'extend_index': 'sentence/background.html'}
        return render(request, "sentence/usermap.html",context)

def user_profile(request):
    if request.session.get('UID'):
        usermodel = User.objects.get(UID=request.session.get('UID'))

        context = {'username': usermodel,'extend_index': 'sentence/background.html'}

        return render(request, "sentence/user_profile.html",context)
    else:
        context = {'extend_index': 'sentence/background.html'}
        return render(request, "sentence/user_profile.html",context)

def get_new_user_icon(request):
    print('in icon save')
    if request.session.get('UID'):
        userpicture = request.GET.get('userPicture')
        if userpicture:
            usermodel = User.objects.get(UID=request.session.get('UID'))
            usermodel.UserIcon = userpicture
            usermodel.save()
        # return render(request, "sentence/user_profile.html",{'username': usermodel})
    else:
       return render(request, "sentence/user_profile.html")


def user_account(request):
    if request.session.get('UID'):
        usermodel = User.objects.get(UID=request.session.get('UID'))

        context = {'username': usermodel,'extend_index': 'sentence/background.html'}

        return render(request, "sentence/user_account.html",context)
    else:
        context = {'extend_index': 'sentence/background.html'}
        return render(request, "sentence/user_account.html",context)

def user_achievement(request):
    if request.session.get('UID'):
        usermodel = User.objects.get(UID=request.session.get('UID'))

        context = {'username': usermodel,'extend_index': 'sentence/background.html'}

        return render(request, "sentence/user_achievement.html",context)
    else:
        context = {'extend_index': 'sentence/background.html'}
        return render(request, "sentence/user_achievement.html",context)

def user_collection(request):
    if request.session.get('UID'):
        get_uid = request.session.get('UID')
        collectionmodel = Collection.objects.filter(UID=get_uid)
        usermodel = User.objects.get(UID=get_uid)

        context = {'username': usermodel,'collection_model': collectionmodel,'extend_index': 'sentence/background.html'}

        return render(request, "sentence/user_collection.html",context)
    else:
        context = {'extend_index': 'sentence/background.html'}
        return render(request, "sentence/user_collection.html",context)

def user_history(request):
    if request.session.get('UID'):
        get_uid = request.session.get('UID')
        usermodel = User.objects.get(UID=get_uid)
        sentencemodel = Sentence.objects.filter(UID=get_uid)
        translationmodel = Translation.objects.filter(UID=get_uid)

        context = {'sentence_model': sentencemodel,'translation_model': translationmodel,
        'username': usermodel,'extend_index': 'sentence/background.html'}

        return render(request, "sentence/user_history.html",context)
    else:
        context = {'extend_index': 'sentence/background.html'}
        return render(request, "sentence/user_history.html",context)



def login_app(request):
    sentencemodel_date_order = Sentence.objects.filter().order_by('-Date')[:12]
    sentencemodel_like_order = Sentence.objects.filter().order_by('-Likes')[:12]
    get_email = request.POST.get('email')
    #app login
    if User.objects.filter(Email=get_email).exists():
        m = User.objects.get(Email=get_email)
        #login
        if m.Password == request.POST.get('password'):
            request.session['UID'] = m.UID
            print(m.UserName)

            context = {'username': m,'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,
            'extend_index': 'sentence/background.html'}
            
            return render(request, 'sentence/index_afterlogin.html',context) 
        #login failed
        else:
            print('Password WRONG')

            context = {'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,'extend_index': 'sentence/background.html'}

            return render(request, 'sentence/index.html',context)
    #social login
    elif request.GET.get('userId'):
        if request.method == 'GET':
            username = request.GET.get('username')
            userId = request.GET.get('userId')
            useremail = request.GET.get('email')
            
            password = '000'
            if User.objects.filter(SocialID = userId).exists():
                # print('in fb session')
                request.session['UID'] = User.objects.get(SocialID = userId).UID
                # limit userId found to 0 object
                user = User.objects.filter(SocialID = userId)[0]
                # user.user_picture = userpicture
                user.save()
            else:
                
                if useremail:
                    new_user_model = User.objects.create(
                        # UID = userId,
                        UserName =  username,
                        Password = password,
                        SocialID = userId,
                        Email = useremail,
                    )
                else:
                    print('fb email not confirm')
                
            context = {'username': username,'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,
            'extend_index': 'sentence/background.html'}
            
            return render(request, 'sentence/index_afterlogin.html',context) 
    #sign up
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

            context = {'username': new_user_model,'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,'extend_index': 'sentence/background.html'}
            
            return render(request, 'sentence/index_afterlogin.html',context)
            
        else:
            print('wrong form')

            context = {'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,'extend_index': 'sentence/background.html'}
            
            return render(request, 'sentence/index.html',context)

        context = {'sentence_content': sentencemodel_like_order,'sentence_content_date': sentencemodel_date_order
        ,'extend_index': 'sentence/background.html'}
        
        return render(request, 'sentence/index.html',context)            

#FB
# def getuserid(request):
#     sentencemodel_date_order = Sentence.objects.filter().order_by('-Date')[:12]
#     sentencemodel_like_order = Sentence.objects.filter().order_by('-Likes')[:12]
#     if request.method == 'GET':
#         username = request.GET.get('username')
#         userId = request.GET.get('userId')
#         useremail = request.GET.get('useremail')
        
#         password = '000'
#         if User.objects.filter(SocialID = userId).exists():
#             # print('in session')
#             request.session['UID'] = User.objects.get(SocialID = userId).UID
#             # limit userId found to 0 object
#             user = User.objects.filter(SocialID = userId)[0]
#             # user.user_picture = userpicture
#             user.save()
#         else:
#             print('create')
#             new_user_model = User.objects.create(
#                 # UID = userId,
#                 UserName =  username,
#                 Password = password,
#                 SocialID = userId,
#                 Email = useremail,
#             )

#         context = {'username': username,'sentence_content': sentencemodel_like_order,
#         'sentence_content_date': sentencemodel_date_order,'extend_index': 'sentence/background.html'}
        
#         return render(request, "sentence/index_afterlogin.html",context)

#logout
def logout(request):
    sentencemodel_date_order = Sentence.objects.filter().order_by('-Date')[:12]
    sentencemodel_like_order = Sentence.objects.filter().order_by('-Likes')[:12]
    print("logout")
    django_logout(request)
    context = {'sentence_content': sentencemodel_like_order,'sentence_content_date': sentencemodel_date_order
    ,'extend_index': 'sentence/background.html'}
    return render(request, "sentence/index.html",context)

#likes
def likes_count(request):
    liked = False
    state = False
    if request.method == 'GET':
        sentence_id = request.GET.get('sentence_id')
        sentence = Sentence.objects.get(SID=sentence_id)
        likes = sentence.Likes
        if request.session.get('has_liked_'+str(sentence_id),liked):
            print("unlike")
            state = False
            if sentence.Likes > 0:
                likes = likes - 1
                try:
                    del request.session['has_liked_'+sentence_id]
                    print('session del ' + str(request.session['has_liked_'+sentence_id]))
                except KeyError:
                    print("keyerror")
                sentence.Likes = likes
                sentence.save()
        else:
            state= True
            print("like")
            request.session['has_liked_'+sentence_id] = True
            likes = likes + 1
            sentence.Likes = likes
            sentence.save()   
        data = {'data':likes,'state':state} 
        return HttpResponse(json.dumps(data),liked)
    else:
        return HttpResponse()
#country     
def getCountry(request):
   if request.method == "GET":
        c_code = request.GET.get('country_UpperCode')
        country = Country.objects.get(Country_code = c_code)
        language_id = Country_language.objects.filter(Country_ID=country.Country_ID)
        
        for i in language_id:
            print(i.Language_ID.Language)
            
        return HttpResponse(json.dumps({
                "country": country.Country_name,   
            }))   

#collection
def collection(request):
    isCollect = False
    if request.method == 'GET':
        sid = request.GET.get('sentence_id') 
        uid = request.session.get('UID')
        if Collection.objects.filter(UID=uid,SID=sid).exists():
            isCollect = False
            Collection.objects.filter(UID=uid,SID=sid).delete()             
        else:
            isCollect = True
            usermodel = User.objects.get(UID=uid)
            sentencemodel = Sentence.objects.get(SID= sid)
            new_collectmodel = Collection.objects.create(
                UID = usermodel,
                SID = sentencemodel,
            )
        return HttpResponse(isCollect)

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
