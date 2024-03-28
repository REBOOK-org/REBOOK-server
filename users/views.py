from rest_framework.views import APIView
from .serialiazers import UserSerializer
from rest_framework.response import Response


class SignUp(APIView): 
    permission_classes = []

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'success', 'data': serializer.data})
