from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import CommentForm


class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(CreateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/post_form.html"
    fields = ["title", "content"]


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    success_url = reverse_lazy("post_list")


# ======================
# Comment CRUD Views
# ======================

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs["pk"])
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "blog/comment_form.html"

    def get_success_url(self):
        return self.object.post.get_absolute_url()


class CommentDeleteView(DeleteView):
    model = Comment
    template_name = "blog/comment_confirm_delete.html"

    def get_success_url(self):
        return self.object.post.get_absolute_url()
