from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.default, name='default'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page'),
    
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path("logout/", auth_views.LogoutView.as_view(next_page="/login/"), name='logout'),
    path("signup/", views.signup) 
]