from __future__ import unicode_literals

from django.db import models
# from datetime import datetime
from django.utils import timezone
#   Create your models here.

#USER
class User(models.Model):

	UID = models.AutoField(primary_key=True)
	UserName = models.CharField(max_length=50, null=False)
	Email = models.EmailField(max_length=254,unique = True)
	Password = models.CharField(max_length=50, null=False)
	SocialID = models.BigIntegerField(null=True,unique = True)
# 	UserIcon = models.ImageField(upload_to='UserIcon_folder',height_field=700,width_field=700,max_length=100)
	#IconPosition = models.
	# EXP = models.IntegerField()
	# Money = models.DecimalField(max_digits=20,decimal_places=0)
# 	language_ID = models.ForeignKey('Language', on_delete=models.CASCADE)

#SENTENCE
class Sentence(models.Model):
	SID = models.AutoField(primary_key=True, null=False, unique=True)
	# SID = models.BigIntegerField(primary_key=True, null=False, unique=True)
	Date = models.DateTimeField(default=timezone.now, blank=True)
	# Date = models.DateTimeField(blank=True)
	Content = models.TextField()
	Sentence_tag = models.TextField()
	Topic_tag = models.TextField()
	UID = models.ForeignKey('User', on_delete=models.CASCADE)

# #TRANSLATION
# class Translation(models.Model):
# 	TID = models.BigIntegerField(primary_key=True, null=False, unique=True)
# 	#Date = models.
# 	Content = models.TextField()
# 	SID = models.ForeignKey('Sentence', on_delete=models.CASCADE)
# 	UID = models.ForeignKey('User', on_delete=models.CASCADE)

# #LANGUAGE
# class Language(models.Model):
# 	Language_ID = models.BigIntegerField(primary_key=True, null=False, unique=True)
# 	Language = models.CharField(max_length=20)

#USER-LANGUAGE
#class User_language(models.Model):
#    Language_ID = models.ForeignKey('Language', on_delete=models.CASCADE)
# 	UID = models.ForeignKey('User', on_delete=models.CASCADE)
#   
#FRIENDSHIP
#class Friendship(models.Model):
#    AreFriends = models.IntegerField()
# 	UID1 = models.ForeignKey('User', on_delete=models.CASCADE)
#    UID2 = models.ForeignKey('User', on_delete=models.CASCADE)
#    
#ACHIEVEMENT
#class Achievement(models.Model):
#    Achievement_ID = models.BigIntegerField(primary_key=True, null=False, unique=True)
# 	UID = models.ForeignKey('User', on_delete=models.CASCADE)
#  
#PAINT_TOOLS
#class Paint_tools(models.Model):
#    Paint_tool_ID = models.BigIntegerField(primary_key=True, null=False, unique=True)
# 	UID = models.ForeignKey('User', on_delete=models.CASCADE)
#
#RANK_SENTENCE
#class Rank_sentence(models.Model):
# 	UID = models.ForeignKey('User', on_delete=models.CASCADE)
#    SID = models.ForeignKey('Sentence', on_delete=models.CASCADE)
# 
#RANK_TRANSLATION
#class Rank_translation(models.Model):
# 	UID = models.ForeignKey('User', on_delete=models.CASCADE)
#    TID = models.ForeignKey('Translation', on_delete=models.CASCADE)
#    
#AREA_LANGUAGE
#class Area_language(models.Model):
# 	Language_ID = models.ForeignKey('Language', on_delete=models.CASCADE)
#    Area_ID = models.ForeignKey('Area', on_delete=models.CASCADE)
#    
#COUNTRY_AREA
#class Country_area(models.Model):
# 	Country_ID = models.ForeignKey('Country', on_delete=models.CASCADE)
#    Area_ID = models.ForeignKey('Area', on_delete=models.CASCADE)
#    
#COUNTRY_LANGUAGE
#class Country_language(models.Model):
#    Country_ID = models.ForeignKey('Country', on_delete=models.CASCADE)
# 	Language_ID = models.ForeignKey('Language', on_delete=models.CASCADE)
#    
#COUNTRY
#class Country(models.Model):
#    Country_ID = models.BigIntegerField(primary_key=True, null=False, unique=True)
# 	Country_name = models.CharField(max_length=20)
#    
#AREA
#class Area(models.Model):
#    Area_ID = models.BigIntegerField(primary_key=True, null=False, unique=True)
# 	Area_name = models.CharField(max_length=20)
