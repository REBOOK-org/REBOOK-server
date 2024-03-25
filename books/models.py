from django.db import models
from django.db import models
from users.models import User


class Book(models.Model):
    """
      This book model creating books_book table
    """
    TYPE_OF_SHARING_CHOICES = [
        ('rent', 'Rent'),
        ('sell', 'Sell'),
        ('free', 'Free')
    ]

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('rented', 'Rented'),
        ('sold', 'Sold'),
        ('donated', 'Donated'),
        ('in_exchange', 'In Exchange') #
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
        ('damaged', 'Damaged')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    type_of_sharing = models.CharField(max_length=10, choices=TYPE_OF_SHARING_CHOICES)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    categories = models.ManyToManyField('Categories', related_name='books')
    """
    # # Usage example:
    # category = Category.objects.get(pk=1)
    # # Access the set of books related to this category
    # books_related_to_category = category.books.all()
    """
    def __str__(self):
        return (f'User: {self.owner}, Book: {self.title}')

class Categories(models.Model):
    """
      This Categories model creating books_categories table
    """
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
