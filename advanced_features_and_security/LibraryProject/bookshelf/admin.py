from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book, CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'date_of_birth', 'is_staff')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

def create_groups_and_permissions():
    book_content_type = ContentType.objects.get_for_model(Book)

    # Get or create permissions
    perms = {
        "can_view": Permission.objects.get(codename="can_view", content_type=book_content_type),
        "can_create": Permission.objects.get(codename="can_create", content_type=book_content_type),
        "can_edit": Permission.objects.get(codename="can_edit", content_type=book_content_type),
        "can_delete": Permission.objects.get(codename="can_delete", content_type=book_content_type),
    }

    # Groups
    editors, _ = Group.objects.get_or_create(name="Editors")
    viewers, _ = Group.objects.get_or_create(name="Viewers")
    admins, _ = Group.objects.get_or_create(name="Admins")

    # Assign permissions
    editors.permissions.set([perms["can_edit"], perms["can_create"]])
    viewers.permissions.set([perms["can_view"]])
    admins.permissions.set(perms.values())

# Run when server starts
try:
    create_groups_and_permissions()
except:
    pass
