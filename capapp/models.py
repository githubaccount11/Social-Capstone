from django.db import models
from django.contrib.auth.models import User

class Images(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_images")
    url = models.URLField(max_length=1000)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    profile_image = models.URLField(max_length=1000, blank=True, null=True)
    images = models.ManyToManyField(Images, related_name="image_profile", blank=True)
    age = models.IntegerField(blank=True, null=True)
    display_age = models.BooleanField(default=False)
    lat = models.CharField(max_length=9, blank=True, null=True)
    long = models.CharField(max_length=9, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    display_location = models.BooleanField(default=False)
    phone = models.CharField(max_length=11, blank=True, null=True)
    display_phone = models.BooleanField(default=False)
    email = models.CharField(max_length=50, blank=True, null=True)
    display_email = models.BooleanField(default=False)
    gender = models.CharField(max_length=20, blank=True, null=True)
    display_gender = models.BooleanField(default=False)
    work = models.CharField(max_length=50, blank=True, null=True)
    display_work = models.BooleanField(default=False)
    education = models.CharField(max_length=50, blank=True, null=True)
    display_education = models.BooleanField(default=False)
    birthday = models.DateField()
    display_birthday = models.BooleanField(default=False)
    date_joined = models.DateField(auto_now_add=True, blank=True, null=True)
    display_date_joined = models.BooleanField(default=False)
    friends = models.ManyToManyField(User, related_name="friends_profile", blank=True)
    display_friends = models.BooleanField(default=False)
    unconfirmed = models.ManyToManyField(User, related_name="unconfirmed_profile", blank=True)
    followers = models.ManyToManyField(User, related_name="followers_profile", blank=True)
    display_followers = models.BooleanField(default=False)
    following = models.ManyToManyField(User, related_name="following_profile", blank=True)
    display_following = models.BooleanField(default=False)
    blocked = models.ManyToManyField(User, related_name="blocked_profile", blank=True)
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post")
    public = models.BooleanField(blank=True, null=True)
    private = models.BooleanField(blank=True, null=True)
    text_content = models.CharField(max_length=1000, blank=True, null=True)
    image = models.URLField(max_length=1000, blank=True, null=True)
    video = models.URLField(max_length=1000, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    
class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment")
    text_content = models.CharField(max_length=1000, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)
    parentment = models.ForeignKey('self', on_delete=models.CASCADE, related_name="subments", blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", blank=True, null=True)

class Chat(models.Model):
    users = models.ManyToManyField(User, related_name="user_chat", blank=True)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="user_message")
    text_content = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")