from rest_framework.views import APIView
from .serialiazers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import status


class SignUp(APIView):
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        tokens = TokenObtainPairSerializer().get_token(serializer.instance)
        return Response(
            {
                'message': 'success', 'user': serializer.data,
                'tokens': {
                    'access': str(tokens.access_token), 'refresh': str(tokens)
                }
            }, status.HTTP_201_CREATED
        )


class UpdateUser(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, request):
        id = request.user.id
        user = User.objects.filter(id=id).first()
        if not user:
            return Response({'message': 'User not found'})
        serializer = UserSerializer(
            user, data=request.data, context={'update': True})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'success', 'user': serializer.data})


class AllUsers(APIView):
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['id'] = self.user.id
        data['email'] = self.user.email
        data['name'] = self.user.name
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = response.data
        tokens = response.data
        data = {
            'message': 'success',
            'user': {
                'id': user['id'],
                'email': user['email'],
                'name': user['name']
            },
            'tokens': {
                'access': tokens['access'],
                'refresh': tokens['refresh']
            }
        }
        return Response(data, status.HTTP_200_OK)
