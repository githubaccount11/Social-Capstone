from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('register_profile', views.register_profile, name="register_profile"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('search/<int:page>/<str:search_query>', views.search, name="search"),
    path('profile/<int:user_id>', views.profile, name="profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
]