from django.urls import path
from .views.auth import *
from .views.user_crud import *
from .views.main_pages import *
from .views.manga import *
from .views.chapter import *
from .views.forum import *

urlpatterns = [
   #auth
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout', logout_view, name="logout"),
    path('auth', auth, name="auth"),
    path('create_new_user', create_new_user, name="create_new_user"),
    path('edit/<int:id>', edit, name="edit"),
    path('edit_user/<int:id>', edit_user, name="edit_user"),
    path('user_crud/', user_crud, name="user_crud"),
    path('change_type_of_user/<int:id>', change_type_of_user, name="change_type_of_user"),
    path('delete/<int:id>', delete_user, name="delete"),


    #main pages
    path('', home_view, name="home"),
    path('about/', about, name="about"),
    path('categories/', categories, name="categories"),
    path('categories/<int:id>', categories, name="categories"),

    #manga
    path('manga/', manga, name="manga"),
    path('manga/create-manga/', create_manga, name="create_manga"),
    path('manga/details/<int:id>', details, name="details"),
    path('manga/view-chapter/<int:capitulo>', view_chapter, name="view_chapter"),
    path('manga/<int:id>/create-chapter/', create_chapter, name="create_chapter"),
    path('manga/create-new-manga/', create_new_manga, name='create_new_manga'),
    path('manga/create-new-chapter/<int:id>', create_new_chapter, name='create_new_chapter'),
    path('manga/edit-manga/<int:id>', edit_manga, name='edit_manga'),
    path('manga/update-manga/', update_manga, name='update_manga'),
    path('manga/delete-manga/<int:id>', delete_manga, name='delete_manga'),
    path('manga/chapter/add-new-comment/<int:id>', add_new_comment_for_chapter, name='add_new_comment_for_chapter'),
    path('manga/delete-chapter/<int:id>', delete_chapter, name='delete_chapter'),

    #forum
    path('forum/', forum, name="forum"),
    path('forum/<int:id>', forum_post, name="forum_post"),
    path('create-new-forum-post/', create_new_forum_post, name='create_new_forum_post'),
    path('add-comment-in-forum-post/<int:id>', add_comment_in_forum_post, name='add_comment_in_forum_post'),
    path('remove-forum-post/<int:id>', remove_forum_post, name='remove_forum_post'),
    path('remove-comment-in-forum-post/<int:id>', remove_comment_in_forum_post, name='remove_comment_in_forum_post')
]