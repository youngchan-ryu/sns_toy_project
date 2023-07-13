from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

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

class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('posts:home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ['title', 'content']
    success_url = reverse_lazy('posts:home')

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = "posts/post_delete.html"
    success_url = reverse_lazy('posts:home')

# def home_view(request):
#     return render(request, 'posts/home.html', {})
