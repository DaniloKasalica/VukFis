from django.shortcuts import render
from scraping import scraping

from rest_framework.views import APIView
from rest_framework import authentication, permissions,status
from rest_framework.response import Response
# Create your views here.
class GetData(APIView):
    authentication_classes=[]
    permission_classes = ()
    def post(self, request):
        data = scraping.finddata(request.data["url"])
        return Response({"data":data}, status=status.HTTP_200_OK)

