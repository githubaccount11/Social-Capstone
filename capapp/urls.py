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
    path('block/<int:user_id>', views.block, name="block"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('', views.index, name="index"),
    path('edit_post/<int:post_id>', views.edit_post, name="edit_post"),
    path('comments/<int:post_id>', views.comments, name="comments"),
    path('make_comment/<int:post_id>/', views.make_comment, {'comment_id': 0}, name="make_comment"),
    path('make_comment/<int:post_id>/<int:comment_id>', views.make_comment, name="make_comment"),
    path('edit_comment/<int:comment_id>', views.edit_comment, name="edit_comment"),
    path('get_comments/<int:post_id>', views.get_comments, name="get_comments")
]