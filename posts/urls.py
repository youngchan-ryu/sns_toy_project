from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path('', views.PostsView.as_view(), name='home'),
    path('<int:pk>/', views.DetailView.as_view(), name='posts_detail'),
    path('new/', views.PostCreateView.as_view(), name='posts_create'),
    path('<int:pk>/edit', views.PostUpdateView.as_view(), name='posts_update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='posts_delete'),
]