from django import forms
from django.forms import ModelForm
from .models import Post, Profile
from datetime import date

class AuthForm(forms.Form):
    username = forms.CharField(max_length=20, label="Username", widget=forms.TextInput(attrs={'placeholder': 'Username:'}))
    password = forms.CharField(max_length=20, label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password:'}))
    first_name = forms.CharField(max_length=20, label="First Name", required=False)
    last_name = forms.CharField(max_length=20, label="Last Name", required=False)
    
class DateInput(forms.DateInput):
    input_type = "date"

class ProfileForm(ModelForm):
    def clean_birthday(self):
        dob = self.cleaned_data['birthday']
        age = (date.today() - dob).days / 365
        if age < 13:
            raise forms.ValidationError('You must be at least 13 years old')
        return dob

    class Meta:
        model = Profile
        fields = ['profile_image', 'age', 'display_age', 'lat', 'long', 'location', 'display_location', 'phone', 'display_phone', 'email', 'display_email', 'gender', 'display_gender', 'work', 'display_work', 'education', 'display_education', 'birthday', 'display_birthday', 'display_date_joined', 'display_friends', 'display_followers', 'display_following']
        widgets = {
           'birthday': DateInput(),
           'profile_image': forms.TextInput(attrs={'placeholder': 'Profile Image:'}),
           'age': forms.TextInput(attrs={'placeholder': 'Profile Image:'}),
           'location': forms.TextInput(attrs={'placeholder': 'Location:'}),
           'phone': forms.TextInput(attrs={'placeholder': 'Phone:'}),
           'email': forms.TextInput(attrs={'placeholder': 'Email:'}),
           'gender': forms.TextInput(attrs={'placeholder': 'Gender:'}),
           'work': forms.TextInput(attrs={'placeholder': 'Work:'}),
           'education': forms.TextInput(attrs={'placeholder': 'Education:'}),
        }

class NewPost(ModelForm):
    class Meta:
        model = Post
        fields = ['public', 'private', 'text_content', 'image', 'video']