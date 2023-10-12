from rest_framework.views import APIView
from rest_framework.response import Response
from .my_auch import *

class index(APIView):
    authentication_classes = []
    def get(self,request):
        return Response({ "code":"200", "moey":"OK", })

class my_class(APIView):
    def get(self,request):
        return Response({ "code":"200", "moey":"OK", })
