from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

# If you created a CustomUser model in accounts/models.py,
# you can register it like this ONLY if not already registered.
try:
    admin.site.register(User)
except admin.sites.AlreadyRegistered:
    pass
