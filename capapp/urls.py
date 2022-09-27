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
    path('delete_post/<int:post_id>', views.delete_post, name="delete_post"),
    path('delete_image/<int:image_id>', views.delete_image, name="delete_image"),
    path('comments/<int:post_id>', views.comments, name="comments"),
    path('make_comment/<int:post_id>/', views.make_comment, {'comment_id': 0}, name="make_comment"),
    path('make_comment/<int:post_id>/<int:comment_id>', views.make_comment, name="make_comment"),
    path('edit_comment/<int:comment_id>', views.edit_comment, name="edit_comment"),
    path('delete_comment/<int:comment_id>', views.delete_comment, name="delete_comment"),
    path('get_comments/<int:post_id>', views.get_comments, name="get_comments"),
    path('get_friends_followers_following/<int:user_id>', views.get_friends_followers_following, name="get_friends_followers_following"),
    path('chat/<int:friend_id>', views.chat, name="chat"),
    path('get_messages/<int:friend_id>', views.get_messages, name="get_messages"),
    path('send_message/<int:friend_id>/<str:message_content>', views.send_message, name="send_message")
]