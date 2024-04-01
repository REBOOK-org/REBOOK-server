from rest_framework import serializers
from .models import Book, Categories, BookImage


class BookSerializer(serializers.ModelSerializer):
    owner_name = serializers.SerializerMethodField()
    category_names = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    # images = serializers.ImageField(source='image.image')

    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'categories': {'write_only': True}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.context.get('update', False):
            for field_name, field in self.fields.items():
                field.required = False

    def get_owner_name(self, obj):
        return obj.owner.name if obj.owner else None

    def get_category_names(self, obj):
        return [category.name for category in obj.categories.all()] if obj.categories.all() else []

    def get_images(self, obj):
        # return [image.image.url for image in obj.book_images.all()] if obj.book_images.all() else []
        return BookImage.objects.filter(book=obj.id).values_list('image', flat=True)


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookImage
        fields = '__all__'
