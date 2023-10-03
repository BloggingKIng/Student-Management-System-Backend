from django.shortcuts import render

# Create your views here.
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import AccessToken
from .models import CustomUser
from .serializers import UserSerializers
from rest_framework_simplejwt.authentication import JWTAuthentication



JWT_authenticator = JWTAuthentication()
class BlacklistRefreshView(APIView):
    def post(self, request):
        try:
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()
            return Response("Logout Successful!")
        except TokenError as e:
            print(e)
            return Response(str("You Are Not Authorized"),status=status.HTTP_400_BAD_REQUEST)

class GetUser(APIView):
    def post(self, request):
        response = JWT_authenticator.authenticate(request)
        if response is not None:
            # unpacking
            user , token = response
            serializer = UserSerializers(user)
            return Response(serializer.data)
        else:
            print("Here")
            return Response("no token is provided in the header or the header is missing",status=status.HTTP_400_BAD_REQUEST)