from django.shortcuts import render
from .models import SchoolInformation
from .serializers import SchoolInformationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import time
# Create your views here.

@api_view(['GET'])
def get_school_info(request):
    school_info = SchoolInformation.objects.all()
    school_info = school_info[0] if len(school_info) > 0 else []
    serializer = SchoolInformationSerializer(school_info)
    return Response({'school_info': serializer.data},status=status.HTTP_200_OK)