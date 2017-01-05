from django.contrib import admin
from .models import User, Sentence, Translation, Topic

admin.site.register(User)
admin.site.register(Sentence)
admin.site.register(Translation)
admin.site.register(Topic)
# Register your models here.
