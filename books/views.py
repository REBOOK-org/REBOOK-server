from rest_framework.views import APIView
from .serialiazers import BookSerializer, ImageSerializer, CategoriesSerializer
from rest_framework.response import Response
from .models import Book, Categories
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status


class Books(APIView):
    """
    This view is for getting all books and creating a new book
    """
    permission_classes = []

    def get(self, request):
        q = request.query_params.get('q', None)
        if q:
            print(q)
            books = Book.objects.filter(name__icontains=q)
            serializer = BookSerializer(books, many=True)
            return Response(serializer.data)

        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        images = request.data.get('images', [])
        if images:
            images = request.data.pop('images')

        owner_id = request.user.id
        request.data['owner'] = owner_id

        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        for image in images:
            image_serializer = ImageSerializer(
                data={'book': serializer.instance.id, 'image': image})
            image_serializer.is_valid(raise_exception=True)
            image_serializer.save()

        return Response({'book': serializer.data}, status=status.HTTP_201_CREATED)


class BookDetails(APIView):
    """
    This view is for getting a single book
    """
    permission_classes = []

    def get(self, request, id):
        book = Book.objects.filter(id=id).first()
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteBook(APIView):
    """
    This view is for deleting a book
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def delete(self, request, id):
        owner_id = request.user.id
        if not Book.objects.filter(id=id, owner=owner_id).exists():
            return Response({'message': 'You are not allowed to delete this book'})
        book = Book.objects.filter(id=id).first()
        book.delete()
        return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class UpdateBook(APIView):
    """
    This view is for updating a book
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, request, id):
        owner_id = request.user.id
        if not Book.objects.filter(id=id, owner=owner_id).exists():
            return Response({'message': 'You are not allowed to update this book'})
        book = Book.objects.filter(id=id).first()
        serializer = BookSerializer(
            book, data=request.data, context={'update': True})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserBooks(APIView):
    """
    This view is for getting all books of a user
    """
    permission_classes = []

    def get(self, request, id):
        books = Book.objects.filter(owner=id)
        serialiazer = BookSerializer(books, many=True)
        return Response(serialiazer.data, status=status.HTTP_200_OK)


class CategoriesList(APIView):
    """
    This view is for getting all categories
    """
    permission_classes = []

    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response({'categories': serializer.data}, status=status.HTTP_200_OK)
