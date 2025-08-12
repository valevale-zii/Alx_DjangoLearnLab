# BASE_DIR exists by default in new projects
STATIC_URL = '/static/'
# If you want a folder for project-level static files:
STATICFILES_DIRS = [BASE_DIR / "static"]   # requires Python3.9 Path style or use os.path.join
