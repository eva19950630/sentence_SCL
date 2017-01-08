from django.contrib import admin
from .models import User, Sentence, Translation, Topic, Friendship, Rank_sentence

admin.site.register(User)
admin.site.register(Sentence)
admin.site.register(Translation)
admin.site.register(Topic)
admin.site.register(Friendship)
admin.site.register(Rank_sentence)
# Register your models here.
