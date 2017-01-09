from django.shortcuts import render
#google+
from .forms import AddUser, PostSentence, PostTranslate, PostTopic
from .models import User, Sentence, Translation, Topic, Country, Country_language, Language, Collection, Friendship, Rank_sentence
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
    sentencemodel_date_order = Sentence.objects.filter().order_by('-Date')[:8]
    sentencemodel_like_order = Sentence.objects.filter().order_by('-Likes')[:8]

    # translation_count = []
    # for s in Sentence.objects.filter().count():
    # # translation_count = [Translation.objects.filter(SID=s.SID).count() for s in sentencemodel_date_order]
    #     translation_count[s.SID] = Translation.objects.filter(SID=s.SID).count()
    #     print(s)

    uid = request.session.get('UID')

    if User.objects.filter(UID = uid).exists():
        if request.session.get('UID'):
            print('login index')
            
            usermodel = User.objects.get(UID=request.session['UID'])

            context = {'username': usermodel,'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,'extend_index': 'sentence/background.html'}

            return render(request, "sentence/index.html",context)
        
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
    trans_code = ""
    # print('sentence_url called')
    sentencemodel = Sentence.objects.get(SID = int(sid))
    new_region_code =  getCountryByLanguage(sentencemodel.Sentence_tag)
    if request.session.get('json_trans_country'): 
        trans_code = request.session.get('json_trans_country')
        del request.session['json_trans_country']
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
            'collect':collectionmodel,'region_code':new_region_code,'trans_region_code':trans_code}
        else:
            context = {'sentence_content': sentencemodel,'username': usermodel,
            'liked': liked,'extend_index': 'sentence/background.html','collected': isCollect,'region_code':new_region_code,'trans_region_code':trans_code}
        del trans_code    
        return render(request, 'sentence/sentence.html',context)
    else:
        context = {'sentence_content': sentencemodel,'extend_index': 'sentence/background.html','region_code':new_region_code,'trans_region_code':trans_code}
        del trans_code
        return render(request, 'sentence/sentence.html',context)

def sentence_post(request):
    # print('sentence_post called')
    # print(sid)
    global region_code
    if request.method == 'POST':
        django_form = PostSentence(request.POST)
        get_uid = request.session.get('UID')
        usermodel = User.objects.get(UID=get_uid)

        if django_form.is_valid():
            if django_form.data.get("topic"):
                new_sentence = django_form.data.get("sentence")
                new_sentence_tag = django_form.data.get("language")
                new_sentence_topic = django_form.data.get("topic")
                new_sentence_link = django_form.data.get("link")
                
                region_code = []
                language_id = Language.objects.get(Language=django_form.data.get("language")).Language_ID
                request.session['region_code']=getCountryByLanguage(language_id)
                
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
                new_sentence_tag = django_form.data.get("language")

                
                
                 
                if User.objects.filter(UID = get_uid).exists():
                    """ This is how your model connects to database and create a new member """
                    new_sentence_model = Sentence.objects.create(
                        Content = new_sentence,
                        Sentence_tag =  new_sentence_tag, 
                        UID = usermodel,
                    )            

                print("daily sentence  store " + str(new_sentence_model.SID))
            
                return HttpResponseRedirect(reverse('sentence_url',kwargs={'sid': new_sentence_model.SID,
                }))
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
                new_translation_tag = django_form.data.get("translation_tag")

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
                    
                Translation_model =  Translation.objects.filter(SID=sentencemodel.SID)   
                Translation_count = Translation_model.count()
                Translation_country = []
                for t_model in Translation_model:
                    if  getCountryByLanguage(t_model.Translation_tag) in         Translation_country:
                        """do nothing"""
                    else:
                        Translation_country.append(getCountryByLanguage(t_model.Translation_tag))
                        
                json_translation_country = json.dumps(Translation_country)
                del Translation_country
                
                try:
                    del request.session['json_trans_country']
                    print('session del ' + str(request.session['json_trans_country']))
                except KeyError:
                    print("keyerror")
               
                request.session['json_trans_country'] = json_translation_country
                
                print(json_translation_country)
                
                sentencemodel.Translation_count = Translation_count
                sentencemodel.save()  

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
        friendlist = Friendship.objects.filter(UID=request.session.get('UID'))
        sentencemodel = None
        if Sentence.objects.filter(UID=request.session.get('UID')).exists():
            sentencemodel = Sentence.objects.filter(UID=request.session.get('UID')).order_by('-Date')[0]
        
        context = {'username': usermodel,'extend_index': 'sentence/background.html','friendlist': friendlist
            ,'sentence':sentencemodel
        }

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
        sentencemodel = Sentence.objects.filter(UID=usermodel.UID).count()
        translationmodel = Translation.objects.filter(UID=usermodel.UID).count()
        
        context = {'username': usermodel,'sentencemodel':sentencemodel,'extend_index': 'sentence/background.html'
            ,'translationmodel':translationmodel
        }

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
    sentencemodel_date_order = Sentence.objects.filter().order_by('-Date')[:8]
    sentencemodel_like_order = Sentence.objects.filter().order_by('-Likes')[:8]
    get_email = request.POST.get('email')

    #social login
    if request.GET.get('userId'):
        if request.method == 'GET':
            username = request.GET.get('username')
            userId = request.GET.get('userId')
            useremail = request.GET.get('email')
            userpucture = request.GET.get('userpucture')
            print(userpucture)
            
            userfriend = request.GET.getlist('friends[]')
            print(userfriend)
            password = '000'
            if User.objects.filter(SocialID = userId).exists():
                # print('in fb session')
                request.session['UID'] = User.objects.get(SocialID = userId).UID
                # limit userId found to 0 object
                user = User.objects.filter(SocialID = userId)[0]
                # user.user_picture = userpicture
                user.save()
                
                #save friends
                if userfriend:
                    for f in userfriend:
                        if User.objects.filter(SocialID=f).exists():
                            userfriend_UID = User.objects.filter(SocialID=f)[0]
                        
                            if not Friendship.objects.filter(UID=user.UID,Friend=userfriend_UID).exists():
                                friendshipmodel = Friendship.objects.create(
                                    AreFriends = 1,
                                    UID = user,
                                    Friend = userfriend_UID,
                                )
                
            else:
                
                if useremail:
                    new_user_model = User.objects.create(
                        # UID = userId,
                        UserName =  username,
                        Password = password,
                        SocialID = userId,
                        Email = useremail,
                        UserIcon = userpucture,
                        # UserIcon = "http://graph.facebook.com/"+userId+"/picture?type=square",
                    )
                    
                    #save friends
                if userfriend:
                    for f in userfriend:
                        if User.objects.filter(SocialID=f).exists():
                            userfriend_UID = User.objects.filter(SocialID=f)[0]
                        
                            if not Friendship.objects.filter(UID=new_user_model.UID,Friend=userfriend_UID).exists():
                                friendshipmodel = Friendship.objects.create(
                                    AreFriends = 1,
                                    UID = new_user_model,
                                    Friend = userfriend_UID,
                                )
                else:
                    print('fb email not confirm')
                
            context = {'username': username,'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,
            'extend_index': 'sentence/background.html'}
            
            return render(request, 'sentence/index.html',context) 
    #sign up
    elif request.POST.get('name') and not User.objects.filter(Email=get_email).exists():
        print('NOT USER')
        django_form = AddUser(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            new_member_email = django_form.data.get("email")
            new_member_password = django_form.data.get('password')
            # new_member_language = django_form.data.get('language')
            # new_uid = str(len(User.objects.all()) + 1)
           
            """ This is how your model connects to database and create a new member """
            new_user_model=User.objects.create(
                # UID = new_uid,
                UserName =  new_member_name, 
                Email = new_member_email,
                Password = new_member_password,
                # NativeLanguage = new_member_language,
            )
                
            request.session['UID'] = new_user_model.UID

            context = {'username': new_user_model,'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,'extend_index': 'sentence/background.html'}
            
            return render(request, 'sentence/index.html',context)
            
        else:
            print('wrong form')

            context = {'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,'extend_index': 'sentence/background.html'}
            
            return render(request, 'sentence/index.html',context)

        context = {'sentence_content': sentencemodel_like_order,'sentence_content_date': sentencemodel_date_order
        ,'extend_index': 'sentence/background.html'}
        
        return render(request, 'sentence/index.html',context)    
    #app login
    elif User.objects.filter(Email=get_email).exists():
        m = User.objects.get(Email=get_email)
        #login
        if m.Password == request.POST.get('password'):
            request.session['UID'] = m.UID
            print(m.UserName)

            context = {'username': m,'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,
            'extend_index': 'sentence/background.html'}
            
            return render(request, 'sentence/index.html',context) 
        #login failed
        else:
            print('Password WRONG')

            context = {'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,'extend_index': 'sentence/background.html'}

            return render(request, 'sentence/index.html',context)  
    else:
        context = {'sentence_content': sentencemodel_like_order,
            'sentence_content_date': sentencemodel_date_order,'extend_index': 'sentence/background.html'}
        return render(request, 'sentence/index.html',context)      

#logout
def logout(request):
    sentencemodel_date_order = Sentence.objects.filter().order_by('-Date')[:8]
    sentencemodel_like_order = Sentence.objects.filter().order_by('-Likes')[:8]
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
        userid = request.session.get('UID')
        usermodel = User.objects.get(UID=userid)
        
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
                    
                if Rank_sentence.objects.filter(UID=userid,SID=sentence_id).exists():
                    Rank_sentence.objects.filter(UID=userid,SID=sentence_id).delete()
                sentence.Likes = likes
                sentence.save()
        else:
            state= True
            print("like")
            request.session['has_liked_'+sentence_id] = True
            likes = likes + 1
            if not Rank_sentence.objects.filter(UID=userid,SID=sentence_id).exists():
                Rank_sentence.objects.create(
                    UID=usermodel,
                    SID=sentence,
                )
            sentence.Likes = likes
            sentence.save()   
        data = {'data':likes,'state':state} 
        return HttpResponse(json.dumps(data),liked)
    else:
        return HttpResponse()

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
    
    
def getCountryByLanguage(language_model):
        language_id = Language.objects.get(Language=language_model).Language_ID
        country = Country_language.objects.filter(Language_ID=language_id)
        region_code = []
        for i in country:
            region_code.append(i.Country_ID.Country_code) 
        json_region_code = json.dumps(region_code)
        
        
        return json_region_code
        
        
def getregion(request):
    if request.method == "GET":
        language = request.GET.get('language')
        language_id = Language.objects.get(Language=language).Language_ID
        country = Country_language.objects.filter(Language_ID=language_id)
        region_code = []
        for i in country:
                region_code.append(i.Country_ID.Country_code)
        region_code = json.dumps({"code": region_code})    
       
        return HttpResponse({ region_code, })
   
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
