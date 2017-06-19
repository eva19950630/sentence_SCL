from django.contrib import admin
from .models import User, Sentence, Translation, Topic, Friendship, Rank_sentence


class user(admin.ModelAdmin) :
    list_display = ['UID','UserName', 'UserIcon','NativeLanguage','Email','Password','SocialID']
    class Meta : 
        model = User
class sentence(admin.ModelAdmin) :
    list_display = ['SID','Date', 'Content','Sentence_tag','TopicID','UID','Likes','Views','Translation_count']
    class Meta : 
        model = Sentence
class translation(admin.ModelAdmin) :
    list_display = ['TID','Date', 'Content','Translation_tag','SID','UID','Likes','Views']
    class Meta : 
        model = Translation
class topic(admin.ModelAdmin) :
    list_display = ['TopicID','Topic_tag', 'Link','Likes','Views']
    class Meta : 
        model = Topic
class friendship(admin.ModelAdmin) :
    list_display = ['AreFriends','UID','Friend']
    class Meta : 
        model = Friendship
class rank_sentence(admin.ModelAdmin) :
    list_display = ['UID','TID']
    class Meta : 
        model = Rank_sentence
admin.site.register(User,user)
admin.site.register(Sentence,sentence)
admin.site.register(Translation,translation)
admin.site.register(Topic,topic)
admin.site.register(Friendship,friendship)
admin.site.register(Rank_sentence,rank_sentence)
# Register your models here.


      
