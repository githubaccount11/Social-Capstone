from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import AuthForm, NewPost, ProfileForm
from .models import Post, Profile
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
def register(request):
    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            auth.login(request, user)
            return redirect('../register_profile')
    context = {
        'form': AuthForm(),
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
    if request.user.is_anonymous:
        return redirect('login')
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(Profile, user=user)
    if user != request.user:
        friend = "Friend"
        follower = False
        if profile.friends.filter(id=request.user.id):
            friend = "Unfriend"
        else:
            your_profile = Profile.objects.filter(user=request.user)[0]
            if your_profile.unconfirmed.filter(id=user_id):
                friend = "Confirm"
            else:
                if profile.unconfirmed.filter(id=request.user.id):
                    friend = "Unsend"
        if profile.followers.filter(id=request.user.id):
            follower = True
        if not profile.display_age:
            profile.age = ""
        if not profile.display_location:
            profile.location = ""
        if not profile.display_phone:
            profile.phone = ""
        if not profile.display_email:
            profile.email = ""
        if not profile.display_gender:
            profile.gender = ""
        if not profile.display_work:
            profile.work = ""
        if not profile.display_education:
            profile.education = ""
        if not profile.display_birthday:
            profile.birthday = ""
        if not profile.display_date_joined:
            profile.date_joined = ""
        if not profile.display_friends:
            profile.friends.set([])
        if not profile.display_followers:
            profile.followers.set([])
        if not profile.display_following:
            profile.following.set([])
        
        context = {
            "user" : user,
            "profile": profile,
            "friend": friend,
            "follower": follower
        }
    else:
        context = {
            "user" : user,
            "profile": profile
        }
    return render(request, 'capapp/profile.html', context)

@login_required
def edit_profile(request):
    if request.user.is_anonymous:
        return redirect('../login')
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
    print("1")
    if request.method == "POST":
        print(2)
        form = AuthForm(request.POST)
        if form.is_valid():
            print(3)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            print(user)
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
    print(users)
    # users = users.exclude(username=request.user.username)
    for index in range(len(list(users.values()))):
        if list(users.values())[index]["username"] == request.user.username:
            list(users.values()).pop(index)
    results = list(users.values("first_name", "last_name", "id", "user_profile__profile_image"))
    print(results)
    return JsonResponse({"data": results})

def friend(request, user_id):
    profile = Profile.objects.filter(user=request.user)[0]
    other_profile = Profile.objects.filter(user__id=user_id)[0]
    friend = profile.friends.filter(id=user_id)
    if friend:
        profile.friends.remove(friend[0])
        other_profile.friends.remove(request.user)
    else:
        unconfirmed = profile.unconfirmed.filter(id=user_id)
        if unconfirmed:
            profile.unconfirmed.remove(unconfirmed[0])
            profile.friends.add(User.objects.filter(id=user_id)[0])
            other_profile.friends.add(request.user)
        else:
            your_unconfirmed = other_profile.unconfirmed.filter(id=request.user.id)
            if your_unconfirmed:
                other_profile.unconfirmed.remove(your_unconfirmed[0])
            else:
                other_profile.unconfirmed.add(request.user)
    profile.save()
    other_profile.save()
    return redirect(f'../profile/{user_id}')

def follow(request, user_id):
    profile = Profile.objects.filter(user=request.user)[0]
    other_profile = Profile.objects.filter(user__id=user_id)[0]
    followee = profile.following.filter(id=user_id)
    if followee:
        profile.following.remove(followee[0])
        other_profile.followers.remove(request.user)
    else:
        profile.following.add(User.objects.filter(id=user_id)[0])
        other_profile.followers.add(request.user)
    profile.save()
    other_profile.save()
    return redirect(f'../profile/{user_id}')

def index(request):
    if request.method == "POST":
        form = NewPost(request.POST)
        if form.is_valid():
            post = Post()
            post.text_content = form.cleaned_data['text_content']
            post.user = request.user
            post.public = form.cleaned_data['public']
            post.private = form.cleaned_data['private']
            post.image = form.cleaned_data['image']
            post.video = form.cleaned_data['video']
            post.save()
        return redirect('../index')
    feed = Post.objects.filter(Q(user__in=request.user.user_profile.following) & Q(public=True))
    feed += Post.objects.filter(Q(user__in=request.user.user_profile.friends) & Q(private=True))
    feed = feed.sort(key = lambda x:x['date_created'])
    context = {
        'form': NewPost,
        'feed': feed
    }
    return render(request, 'capapp/index.html', context)
