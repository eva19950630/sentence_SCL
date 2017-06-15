from django.contrib import admin
from .models import User, Sentence, Translation, Topic, Friendship, Rank_sentence


class user(admin.ModelAdmin) :
    list_display = ['UID','UserName', 'UserIcon','NativeLanguage','Email','Password','SocialID']
    class Meta : 
        model = User
admin.site.register(User,user)
admin.site.register(Sentence)
admin.site.register(Translation)
admin.site.register(Topic)
admin.site.register(Friendship)
admin.site.register(Rank_sentence)
# Register your models here.


      
