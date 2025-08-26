from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_list(request):
    query = request.GET.get("q")
    if query:
        posts = Post.objects.filter(
            title__icontains=query
        ) | Post.objects.filter(
            content__icontains=query
        ) | Post.objects.filter(
            tags__name__icontains=query
        )
        posts = posts.distinct()
    else:
        posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = CommentForm()
    return render(request, "blog/post_detail.html", {"post": post, "comments": comments, "form": form})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")
    else:
        form = PostForm()
    return render(request, "blog/post_form.html", {"form": form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/post_form.html", {"form": form})
