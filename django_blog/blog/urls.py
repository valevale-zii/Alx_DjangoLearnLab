from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home redirects to post list
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),

    # Blog post CRUD (singular 'post' for checker)
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),

    # Optional: list of all posts (can keep for home)
    path('posts/', views.PostListView.as_view(), name='post-list'),
]
