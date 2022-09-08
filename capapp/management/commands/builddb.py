from django.core.management.base import BaseCommand
import datetime
import random
from capapp.models import User, Profile, Post

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        User.objects.filter(username__contains="testUser").delete()
        
        
        for x in range(100):
            user = User.objects.create_user(f"testUser{x}", '', 'password')
            user.first_name = f'testName{x}'
            user.last_name = f'testLName{x}'
            user.save()
           
        for x in range(100): 
            user = User.objects.filter(username__contains="testUser")[x]
            
            profile = Profile()
            profile.profile_image = "https://openclipart.org/image/200px/327179"
            profile.birthday = datetime.date(1997, 10, 19)
            profile.user = user
            profile.save()

        for x in range(100):
            profile = Profile.objects.filter(user__username__contains="testUser")[x]
            
            friends = User.objects.filter(username__contains="testUser")
            friends_to_add = random.choices(friends, k=random.randint(40, 60))
            for friend in friends_to_add:
                profile.friends.add(friend)

            followers = User.objects.filter(username__contains="testUser")
            followers_to_add = random.choices(followers, k=random.randint(40, 60))
            for follower in followers_to_add:
                profile.followers.add(follower)

            following = User.objects.filter(username__contains="testUser")
            following_to_add = random.choices(following, k=random.randint(40, 60))
            for followee in following_to_add:
                profile.following.add(followee)

            profile.save()
            print(f"Created user: testUser{x}")