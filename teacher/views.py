from rest_framework.views import APIView
from rest_framework.response import Response
from .my_auch import *
from .models import *

class index(APIView):
    authentication_classes = []
    def get(self,request):
        return Response({ "code":"200", "moey":"OK", })

class my_class(APIView):
    def get(self,request):
        return Response({ "code":"200", "moey":"OK", "teacher":"22 shigong 1", })
    def post(self,request):
        user = request.get("user")
        pawd = request.get("pawd")
        users = UserInfo()
        users.user = user
        users.pswd = pawd
        users.save()

class a(APIView):
    pass
