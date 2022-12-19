from django.urls import path
from .views.auth import auth, create_new_user, register_view, logout_view, login_view
from .views.main_pages import home_view, details, about, categories
from .views.manga import manga

urlpatterns = [
    path('', home_view, name="home"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout', logout_view, name="logout"),
    path('auth', auth, name="auth"),
    path('create_new_user', create_new_user, name="create_new_user"),
    path('details/', details, name="details"),
    path('about/', about, name="about"),
    path('categories/', categories, name="categories"),
    path('manga/', manga, name="manga"),
]