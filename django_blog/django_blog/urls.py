from django.contrib import admin
from django.urls import path
from blog import views  # Import views from blog app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Homepage route
]
