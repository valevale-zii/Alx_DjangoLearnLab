from rest_framework import serializers
from .models import Book, Author

class BookSerializer(serializers.ModelSerializer):
    # Use PK for create/update (works nicely in tests)
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = "__all__"
