from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('loginfirst/', views.login_first_view, name='login_first'),
]