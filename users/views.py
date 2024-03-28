from rest_framework.views import APIView
from .serialiazers import UserSerializer
from rest_framework.response import Response
from .models import User
from .tokens import create_token_for_user



class SignUp(APIView): 
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    
class Login(APIView):
    permission_classes = []

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        
        if not email or not password:
            return Response({'message': 'Incomplete data'})
        
        user = User.objects.filter(email=email).first()
        if not user:
            return Response({'message': 'Not found'})
        
        if not user.check_password(password):
            return Response({'message': 'Not found'})

        tokens = create_token_for_user(user)
        response = Response()
        response.data = {
            'message': 'success',
            'tokens': tokens
        }
        return response

    
