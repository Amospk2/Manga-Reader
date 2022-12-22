from django.urls import path
from .views.auth import auth, register_view, logout_view, login_view, edit
from .views.user_crud import edit_user, user_crud, change_type_of_user, create_new_user, delete_user
from .views.main_pages import home_view, about, categories
from .views.manga import manga, create_manga, details, create_chapter, view_chapter, create_new_manga, delete_manga
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
    path('about/', about, name="about"),
    path('categories/', categories, name="categories"),

    #manga
    path('manga/', manga, name="manga"),
    path('manga/create-manga/', create_manga, name="create_manga"),
    path('manga/details/<int:id>', details, name="details"),
    path('manga/view-chapter/<int:id>', view_chapter, name="view_chapter"),
    path('manga/<int:id>/create-chapter/', create_chapter, name="create_chapter"),
    path('manga/create-new-manga/', create_new_manga, name='create_new_manga'),
    path('manga/delete-manga/<int:id>', delete_manga, name='delete_manga'),

    #forum
    path('forum/', forum, name="forum"),
    path('forum/<int:id>', forum_post, name="forum_post")
]