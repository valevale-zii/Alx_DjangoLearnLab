from django.urls import path
from . import views

urlpatterns = [
    # Home
    path('', views.home, name='home'),

    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    # Post CRUD (singular 'post' required by checker)
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # List all posts (optional for home)
    path('posts/', views.PostListView.as_view(), name='post-list'),

    # Comment URLs
    path('post/<int:post_id>/comment/new/', views.add_comment, name='comment-add'),
    path('comment/<int:comment_id>/edit/', views.edit_comment, name='comment-edit'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='comment-delete'),
]
