from typing import Tuple
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import AuthForm, ProfileForm
from .models import Post, Profile, Comments, Images
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
def register(request):
    error = ""
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            taken = User.objects.filter(username=form.cleaned_data['username'])
            if not taken:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                )
                auth.login(request, user)
                return redirect('../register_profile')
            else:
                error = "That username is taken"
    context = {
        'form': AuthForm(),
        'error': error
    }
    return render(request, 'capapp/register.html', context)

@login_required
def register_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = Profile()
            profile.user = request.user
            saveForm(profile, form)
            return redirect(f'../profile/{request.user.id}')
    context = {
        'form': ProfileForm(),
    }
    return render(request, 'capapp/register_profile.html', context)

def saveForm(profile, form):
    profile.profile_image = form.cleaned_data['profile_image']
    profile.age = form.cleaned_data['age']
    profile.display_age = form.cleaned_data['display_age']
    profile.location = form.cleaned_data['location']
    profile.display_location = form.cleaned_data['display_location']
    profile.phone = form.cleaned_data['phone']
    profile.display_phone = form.cleaned_data['display_phone']
    profile.email = form.cleaned_data['email']
    profile.display_email = form.cleaned_data['display_email']
    profile.gender = form.cleaned_data['gender']
    profile.display_gender = form.cleaned_data['display_gender']
    profile.work = form.cleaned_data['work']
    profile.display_work = form.cleaned_data['display_work']
    profile.education = form.cleaned_data['education']
    profile.display_education = form.cleaned_data['display_education']
    profile.birthday = form.cleaned_data['birthday']
    profile.display_birthday = form.cleaned_data['display_birthday']
    profile.display_date_joined = form.cleaned_data['display_date_joined']
    profile.display_friends = form.cleaned_data['display_friends']
    profile.display_followers = form.cleaned_data['display_followers']
    profile.display_following = form.cleaned_data['display_following']
    profile.save()

@login_required
def profile(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        profile = Profile.objects.get(user=user)
    except (User.DoesNotExist, Profile.DoesNotExist):
        return render(request, 'capapp/profile_not_found.html')
    
    if request.user in list(profile.blocked.all()):
        return render(request, 'capapp/profile_not_found.html')

    feed = []
    if user == request.user:
        feed = list(Post.objects.filter(user=request.user))
    else:
        friend = profile.friends.filter(id=request.user.id)
        follower = profile.followers.filter(id=request.user.id)
        if friend:
            if follower:
                feed = list(Post.objects.filter(Q(user=user), Q(public=True) | Q(private=True)))
            else:
                feed = list(Post.objects.filter(Q(user=user) & Q(public=True)))
        else:
            if follower:
                feed = list(Post.objects.filter(Q(user=user) & Q(private=True)))
    feed.sort(key = lambda x:x.date_created)
    feed = feed[::-1]

    # print("followers:", profile.followers.all())
    # print("followees:", profile.following.all())
    
    if user != request.user:
        print("users are equivalent")
        your_profile = Profile.objects.get(user=request.user)
        friend = "Friend"
        follower = False
        blocked = False
        if profile.friends.filter(id=request.user.id):
            friend = "Unfriend"
        else:
            if your_profile.unconfirmed.filter(id=user_id):
                friend = "Confirm"
            else:
                if profile.unconfirmed.filter(id=request.user.id):
                    friend = "Unsend"
        if profile.followers.filter(id=request.user.id):
            follower = True
        if your_profile.blocked.filter(id=user_id):
            blocked = True
        #print("profile image:", profile.profile_image)
        print("unconfirmed:", profile.unconfirmed.all())
        context = {
            "user" : user,
            "friend": friend,
            "follower": follower,
            "blocked": blocked,
            "images": profile.images.all(),
        }
        if profile.display_age:
            context["age"] = profile.age
        if profile.display_location:
            context["location"] = profile.location
        if profile.display_phone:
            context["phone"] = profile.phone
        if profile.display_email:
            context["email"] = profile.email
        if profile.display_gender:
            context["gender"] = profile.gender
        if profile.display_work:
            context["work"] = profile.work
        if profile.display_education:
            context["education"] = profile.education
        if profile.display_birthday:
            context["birthday"] = profile.birthday
        if profile.display_date_joined:
            context["date_joined"] = profile.date_joined
        if profile.display_friends:
            context["friends"] = profile.friends.all()
        if profile.display_followers:
            context["followers"] = profile.followers.all()
        if profile.display_following:
            context["following"] = profile.following.all()
    else:
        context = {
            "feed": feed,
            "user": user,
            "images": profile.images.all(),
            "unconfirmed": profile.unconfirmed.all(),
        }
        context["age"] = profile.age
        context["location"] = profile.location
        context["phone"] = profile.phone
        context["email"] = profile.email
        context["gender"] = profile.gender
        context["work"] = profile.work
        context["education"] = profile.education
        context["birthday"] = profile.birthday
        context["date_joined"] = profile.date_joined
        context["friends"] = list(profile.friends.all())
        context["followers"] = list(profile.followers.all())
        context["following"] = list(profile.following.all())
    return render(request, 'capapp/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == "GET":
        try:
            profile = Profile.objects.get(user=request.user)
        except profile.DoesNotExist:
            return redirect(f'../profile/{request.user.id}')
        if request.user == profile.user:
            context = {
                "profile": profile,
                "form": ProfileForm({
                    "profile_image": profile.profile_image,
                    "age": profile.age,
                    "display_age": profile.display_age,
                    "location": profile.location,
                    "display_location": profile.display_location,
                    "phone": profile.phone,
                    "display_phone": profile.display_phone,
                    "email": profile.email,
                    "display_email": profile.display_email,
                    "gender": profile.gender,
                    "display_gender": profile.display_gender,
                    "work": profile.work,
                    "display_work": profile.display_work,
                    "education": profile.education,
                    "display_education": profile.display_education,
                    "birthday": profile.birthday,
                    "display_birthday": profile.display_birthday,
                    "display_date_joined": profile.display_date_joined,
                    "display_friends": profile.display_friends,
                    "display_followers": profile.display_followers,
                    "display_following": profile.display_following})
            }
            return render(request, 'capapp/edit_profile.html', context)
        else:
            return redirect(f'../profile/{request.user.id}')
    elif request.method == "POST":
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            return redirect(f'../profile/{request.user.id}')
        if request.user == profile.user:
            form = ProfileForm(request.POST)
            if form.is_valid():
                saveForm(profile, form)
            return redirect(f'../profile/{request.user.id}')
    return redirect(f'../profile/{request.user.id}')

def login(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                next = request.GET.get('next')
                if next:
                    return redirect(next)
                return redirect(f'../profile/{request.user.id}')
        form.add_error(error="Invalid username or password", field="username")
        context = {
            "form": form
        }
    else:
        context = {
            "form": AuthForm()
        }
    return render(request, 'capapp/login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('login')

def search(request):
    return render(request, 'capapp/search.html')

def search_run(request, page, search_query):
    users = User.objects.filter(Q(username__icontains=search_query) | Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query))[page*30:(page+1)*30]
    # users = users.exclude(username=request.user.username)
    user_list = list(users.values("username", "first_name", "last_name", "id", "user_profile__profile_image", "user_profile"))
    index = 0
    while index < len(user_list):
        if user_list[index]["username"] == request.user.username or request.user in list(Profile.objects.get(id=user_list[index]["user_profile"]).blocked.all()):
            user_list.pop(index)
        else:
            index += 1
    return JsonResponse({"data": user_list})

def friend(request, user_id):
    profile = Profile.objects.get(user=request.user)
    other_profile = Profile.objects.get(user__id=user_id)
    friend = profile.friends.filter(id=user_id)
    if friend:
        #if friends then remove friendship
        profile.friends.remove(friend[0])
        other_profile.friends.remove(request.user)
    else:
        unconfirmed = profile.unconfirmed.filter(id=user_id)
        if unconfirmed:
            #if you haven't confirmed then remove confirm and add friends
            profile.unconfirmed.remove(unconfirmed[0])
            profile.friends.add(User.objects.get(id=user_id))
            other_profile.friends.add(request.user)
        else:
            your_unconfirmed = other_profile.unconfirmed.filter(id=request.user.id)
            if your_unconfirmed:
                #if they haven't confirmed then remove request
                other_profile.unconfirmed.remove(your_unconfirmed[0])
            else:
                #if neither friends nor confirmed send confirmation request
                other_profile.unconfirmed.add(request.user)
    profile.save()
    other_profile.save()
    return redirect(f'../profile/{user_id}')

def follow(request, user_id):
    profile = Profile.objects.get(user=request.user)
    other_profile = Profile.objects.get(user=user_id)
    followee = profile.following.filter(id=user_id)
    if followee:
        print("remove follower")
        profile.following.remove(followee[0])
        other_profile.followers.remove(request.user)
    else:
        print("add follower")
        profile.following.add(User.objects.get(id=user_id))
        other_profile.followers.add(request.user)
    profile.save()
    other_profile.save()
    return redirect(f'../profile/{user_id}')

def block(request, user_id):
    profile = Profile.objects.get(user=request.user)
    blocked = profile.blocked.filter(id=user_id)
    if blocked:
        profile.blocked.remove(blocked[0])
    else:
        profile.blocked.add(User.objects.get(id=user_id))
    profile.save()
    return redirect(f'../profile/{user_id}')

@login_required
def index(request):
    if request.method == "POST":
        form = request.POST
        post = Post()
        post.text_content = form.get('text_content')
        post.user = request.user
        if form.get('public') == 'on':
            post.public = True
        else:
            post.public = False
        if form.get('private') == 'on':
            post.private = True
        else:
            post.private = False
        post.image = form.get('image')
        post.video = form.get('video')
        post.save()
        image = Images()
        image.user = request.user
        image.url = post.image
        image.save()
        profile = Profile.objects.get(user=request.user)
        profile.images.add(image)
        profile.save()
        return redirect('../')
    feed = list(Post.objects.filter(Q(user__in=request.user.user_profile.following.all()) & Q(public=True)))
    feed += list(Post.objects.filter(Q(user__in=request.user.user_profile.friends.all()) & Q(private=True)))
    feed += list(Post.objects.filter(user=request.user))
    index = 0
    while index < len(feed):
        if request.user in list(Profile.objects.get(user=feed[index].user).blocked.all()):
            feed.pop(index)
        else:
            index += 1
    feed.sort(key = lambda x:x.date_created)
    feed = feed[::-1]
    context = {
        'feed': feed
    }
    return render(request, 'capapp/index.html', context)

@login_required
def edit_post(request, post_id):
    if request.method == "GET":
        try:
            post = Post.objects.get(id=post_id)
            if post.user != request.user:
                return redirect('../')
        except post.DoesNotExist:
            return redirect('../')
        if request.user == post.user:
            context = {
                "post": post
            }
            return render(request, 'capapp/edit_post.html', context)
        else:
            return redirect('../')
    elif request.method == "POST":
        try:
            post = Post.objects.get(id=post_id)
            if post.user != request.user:
                return redirect('../')
        except Post.DoesNotExist:
            return redirect('../')
        if request.user == post.user:
            form = request.POST
            if form.get('public') == 'on':
                post.public = True
            else:
                post.public = False
            if form.get('private') == 'on':
                post.private = True
            else:
                post.private = False
            post.text_content = form.get('text_content')
            post.image = form.get('image')
            post.video = form.get('video')
            post.save()
            image = Images()
            image.user = request.user
            image.url = post.image
            image.save()
            profile = Profile.objects.get(user=request.user)
            profile.images.add(image)
            profile.save()
            return redirect('../')
    return redirect('../')

def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.user == request.user:
        post.delete()
    return redirect(f'../')

def delete_image(request, image_id):
    image = Images.objects.get(id=image_id)
    if image.user == request.user:
        image.delete()
    return redirect(f'../profile/{image.user.id}')

def comments(request, post_id):
    profile = Profile.objects.get(user=request.user)
    post = Post.objects.get(id=post_id)
    if post.user == request.user or post.user in profile.friends.all() and post.private or post.user in profile.following.all() and post.public:
        context = {
            'post': post
        }
        return render(request, 'capapp/comments.html', context)
    return redirect('../')

def make_comment(request, post_id, comment_id):
    profile = Profile.objects.get(user=request.user)
    post = Post.objects.get(id=post_id)
    print(request.user.id)
    if post.user == request.user or post.user in profile.friends.all() and post.private or post.user in profile.following.all() and post.public:
        if request.method == "POST":
            form = request.POST
            comment = Comments()
            comment.text_content = form.get('text_content')
            comment.user = request.user
            comment.post = post
            if comment_id != 0:
                comment.parentment = Comments.objects.get(id=comment_id)
            comment.save()
            return redirect('comments', post_id=post_id)
        if comment_id != 0:
            comment = Comments.objects.filter(id=comment_id)
            if comment:
                context = {
                    'post': post,
                    'comment': comment[0]
                }
        else:
            context = {
                'comment': False,
                'post': post
            }
        return render(request, 'capapp/make_comment.html', context)
    return redirect('../../')

def edit_comment(request, comment_id):
    if request.method == "GET":
        try:
            comment = Comments.objects.get(id=comment_id)
            if comment.user != request.user:
                return redirect('../')
        except comment.DoesNotExist:
            return redirect(f'../')
        if request.user == comment.user:
            context = {
                "comment": comment
            }
            return render(request, 'capapp/edit_comment.html', context)
        else:
            return redirect(f'../comments/{comment.post.id}')
    elif request.method == "POST":
        try:
            comment = Comments.objects.get(id=comment_id)
            if comment.user != request.user:
                return redirect('../')
        except Post.DoesNotExist:
            return redirect(f'../comments/{comment.post.id}')
        if request.user == comment.user:
            form = request.POST
            comment.text_content = form.get('text_content')
            comment.save()
            return redirect(f'../comments/{comment.post.id}')
    return redirect(f'../comments/{comment.post.id}')

def delete_comment(request, comment_id):
    comment = Comments.objects.get(id=comment_id)
    if comment.user == request.user:
        comment.delete()
    return redirect(f'../')

def get_comments(request, post_id):
    post = Post.objects.get(id=post_id)
    profile = Profile.objects.get(user=request.user)
    if post.user == request.user or post.user in profile.friends.all() and post.private or post.user in profile.following.all() and post.public:
        comments = []
        # print(post.comments.all())
        for comment in post.comments.all():
            if request.user not in list(Profile.objects.get(user=comment.user).blocked.all()):
                comments.append({
                    'comment': {"id": comment.id, "post_id": comment.post.id, "text_content": comment.text_content, "user__first_name": comment.user.first_name, "user__last_name": comment.user.last_name, "user__id": comment.user.id, "date_created": comment.date_created, "date_edited": comment.date_edited},
                    'subments': get_subments(request, comment.id)
                })
        data = [
            comments,
            request.user.id
        ]
        # print(comments)
        return JsonResponse({"data": data})
    return JsonResponse({"data": ""})

def get_subments(request, comment_id):
    comment = Comments.objects.get(id=comment_id)
    comments = []
    for subment in comment.subments.all():
        if request.user not in list(Profile.objects.get(user=comment.user).blocked.all()):
            comments.append({
                'comment': {"id": subment.id, "post_id": subment.post.id, "text_content": subment.text_content, "user__first_name": subment.user.first_name, "user__last_name": subment.user.last_name, "user__id": subment.user.id, "date_created": subment.date_created, "date_edited": subment.date_edited},
                'subments': get_subments(request, subment.id)
            })
    return comments

def get_friends_followers_following(request, user_id):
    if user_id == request.user.id:
        profile = Profile.objects.get(user=User.objects.get(id=user_id))
        data = {
            'friends': list(profile.friends.all().values("user_profile__profile_image", "first_name", "last_name", "id", "user_profile__lat", "user_profile__long")),
            'followers': list(profile.followers.all().values("user_profile__profile_image", "first_name", "last_name", "id", "user_profile__lat", "user_profile__long")),
            'following': list(profile.following.all().values("user_profile__profile_image", "first_name", "last_name", "id", "user_profile__lat", "user_profile__long"))
        }
        return JsonResponse({"data": data})
    return JsonResponse({"data": ""})