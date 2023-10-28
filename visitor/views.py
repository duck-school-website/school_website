from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class index(APIView):
    def get(self,request):
        return Response({ "code":"200", "moey":"OK", })


