from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class My_authenticate(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get("token")
        if token:
            return ("duck",token)
        raise AuthenticationFailed({ "code":404, "error":"NO" })
        # return super().authenticate(request)
