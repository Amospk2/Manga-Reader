from django.urls import path
from .views.auth import auth, create_new_user, register_view, logout_view, login_view
from .views.home import home_view, details

urlpatterns = [
    path('', home_view, name="home"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('logout', logout_view, name="logout"),
    path('auth', auth, name="auth"),
    path('create_new_user', create_new_user, name="create_new_user"),
    path('details/', details, name="details"),
]