from django.db import models
from users.models import User


class Book(models.Model):
    """
    This book model creating books_book table
    """

    TYPE_OF_SHARING_CHOICES = [
        ('sell', 'Sell'),
        ('free', 'Free')
    ]

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('sold', 'Sold'),
        ('donated', 'Donated'),
        ('in_exchange', 'In Exchange')
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
        ('damaged', 'Damaged')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    exchangeable = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    type_of_sharing = models.CharField(
        max_length=10, choices=TYPE_OF_SHARING_CHOICES)
    status = models.CharField(
        max_length=12, choices=STATUS_CHOICES, default='available')
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    categories = models.ManyToManyField(
        'Categories', related_name='books', default=None, blank=True)

    """
    # # Usage example for related_name:
    # category = Category.objects.get(pk=1)
    # # Access the set of books related to this category
    # books_related_to_category = category.books.all()
    """

    def __str__(self):
        return f'User: {self.owner}, Book: {self.name}'


class Categories(models.Model):
    """
    This Categories model creating books_categories table
    """
    CATEGORY_CHOICES = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('fantasy', 'Fantasy'),
        ('science-fiction', 'Science Fiction'),
        ('horror', 'Horror'),
        ('mystery', 'Mystery'),
    ]

    name = models.CharField(
        max_length=200, choices=CATEGORY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name


class BookImage(models.Model):
    """ This BookImage model creating books_bookimage table
    """

    book = models.ForeignKey(Book, on_delete=models.SET_NULL,
                             null=True, related_name='book_images')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.name} Image'
