from rest_framework import serializers
from .models import Book, Categories

class BookSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()
    category_names = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    def get_owner_name(self, obj):
        return obj.owner.name if obj.owner else None

    def get_category_names(self, obj):
        return [category.name for category in obj.categories.all()] if obj.categories.all() else []

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
