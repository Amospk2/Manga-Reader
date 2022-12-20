from django.urls import path
from .views.auth import auth, register_view, logout_view, login_view, edit
from .views.user_crud import edit_user, user_crud, change_type_of_user, create_new_user, delete_user
from .views.main_pages import home_view, details, about, categories
from .views.manga import manga
from .views.forum import forum, forum_post

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
    path('details/', details, name="details"),
    path('about/', about, name="about"),
    path('categories/', categories, name="categories"),

    #manga
    path('manga/', manga, name="manga"),

    #forum
    path('forum/', forum, name="forum"),
    path('forum/<int:id>', forum_post, name="forum_post")
]