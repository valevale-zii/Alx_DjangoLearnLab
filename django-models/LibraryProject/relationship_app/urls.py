from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views  # 👈 this satisfies "views.register"

urlpatterns = [
    path('register/', views.register_view, name='register'),  # views.register = OK
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),  # OK
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),  # OK
]
