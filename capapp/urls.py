from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('register_profile', views.register_profile, name="register_profile"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('search/', views.search, name="search"),
    path('search/<int:page>/<str:search_query>', views.search_run, name="search_run"),
    path('profile/<int:user_id>', views.profile, name="profile"),
    path('friend/<int:user_id>', views.friend, name="friend"),
    path('follow/<int:user_id>', views.follow, name="follow"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('', views.index, name="index"),
]