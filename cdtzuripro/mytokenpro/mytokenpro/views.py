# myapp/views.py
#from rest_framework.decorators import api_view, authentication_classes, permission_classes
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
#from .models import Note
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import generics, status
from .serializers import SignUpSerializer
from rest_framework.views import APIView


class signUpview(generics.GeneriricAPIView):
    serializer_class = signUpSerializer
    
    def post(self, request: Request):
        data = request.data

        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            Response = {
                "message": "User created successfully",
                "data": serializer
        
            }

            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUESTED)
    
class loginView(APIView):