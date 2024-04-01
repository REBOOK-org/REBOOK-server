from rest_framework.views import APIView
from .serialiazers import BookSerializer, ImageSerializer
from rest_framework.response import Response
from .models import Book, BookImage
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import status


class Books(APIView):
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
        return Response(serializer.data)

    def post(self, request):
        images = request.FILES.getlist('images', [])
        request.data.pop('images')

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

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BookDetails(APIView):
    permission_classes = []

    def get(self, request, id):
        book = Book.objects.filter(id=id).first()
        serializer = BookSerializer(book)
        return Response(serializer.data)


# # class CreateBook(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [JWTAuthentication]

#     def post(self, request):
#         images = request.FILES.getlist('images', [])
#         request.data.pop('images')

#         owner_id = request.user.id
#         request.data['owner'] = owner_id

#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         for image in images:
#             image_serializer = ImageSerializer(
#                 data={'book': serializer.instance.id, 'image': image})
#             image_serializer.is_valid(raise_exception=True)
#             image_serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)


class DeleteBook(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def delete(self, request, id):
        owner_id = request.user.id
        if not Book.objects.filter(id=id, owner=owner_id).exists():
            return Response({'message': 'You are not allowed to delete this book'})
        book = Book.objects.filter(id=id).first()
        book.delete()
        return Response({'message': 'Book deleted successfully'})


class UpdateBook(APIView):
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
        return Response(serializer.data)


class UserBooks(APIView):
    permission_classes = []

    def get(self, request, id):
        books = Book.objects.filter(owner=id)
        serialiazer = BookSerializer(books, many=True)
        return Response(serialiazer.data)
