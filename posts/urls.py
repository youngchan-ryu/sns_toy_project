from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path('', views.PostsView.as_view(), name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='posts_detail'),
]