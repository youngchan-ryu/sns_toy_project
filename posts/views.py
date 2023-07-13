from django.shortcuts import render
from django.views import generic

from .models import Post


# Create your views here.

class PostsView(generic.ListView):
    template_name = "posts/home.html"
    context_object_name = "posts_list"

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")


class DetailView(generic.DetailView):
    model = Post
    template_name = "posts/detail.html"

    def get_queryset(self):
        return Post.objects.all()

# def home_view(request):
#     return render(request, 'posts/home.html', {})
