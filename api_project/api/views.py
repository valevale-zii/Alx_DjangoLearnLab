from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import YourModel

# List view
class YourModelListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = YourModel
    template_name = "yourmodel_list.html"
    permission_required = "api.view_yourmodel"

# Detail view
class YourModelDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = YourModel
    template_name = "yourmodel_detail.html"
    permission_required = "api.view_yourmodel"

# Create view
class YourModelCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = YourModel
    fields = "__all__"
    template_name = "yourmodel_form.html"
    success_url = reverse_lazy("yourmodel_list")
    permission_required = "api.add_yourmodel"

# Update view
class YourModelUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = YourModel
    fields = "__all__"
    template_name = "yourmodel_form.html"
    success_url = reverse_lazy("yourmodel_list")
    permission_required = "api.change_yourmodel"

# Delete view
class YourModelDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = YourModel
    template_name = "yourmodel_confirm_delete.html"
    success_url = reverse_lazy("yourmodel_list")
    permission_required = "api.delete_yourmodel"
