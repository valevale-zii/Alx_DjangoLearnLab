from django.shortcuts import render
from .models import Post  # Import Post model

# Homepage view
def home(request):
    posts = Post.objects.all().order_by('-published_date')  # Get all posts
    return render(request, 'blog/home.html', {'posts': posts})
