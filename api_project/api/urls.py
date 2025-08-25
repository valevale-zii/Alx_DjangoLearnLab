from django.urls import path
from .views import (
    YourModelListView,
    YourModelDetailView,
    YourModelCreateView,
    YourModelUpdateView,
    YourModelDeleteView,
)

urlpatterns = [
    path("yourmodel/", YourModelListView.as_view(), name="yourmodel_list"),
    path("yourmodel/<int:pk>/", YourModelDetailView.as_view(), name="yourmodel_detail"),
    path("yourmodel/create/", YourModelCreateView.as_view(), name="yourmodel_create"),
    path("yourmodel/<int:pk>/update/", YourModelUpdateView.as_view(), name="yourmodel_update"),
    path("yourmodel/<int:pk>/delete/", YourModelDeleteView.as_view(), name="yourmodel_delete"),
]
