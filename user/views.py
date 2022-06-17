from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password


# 회원가입
class SignUp(APIView):
    permission_classes = [permissions.AllowAny] # 누구나 view 조회 가능
    # permission_classes = [permissions.IsAdminUser] # admin만 view 조회 가능
    # permission_classes = [permissions.IsAuthenticated] # 로그인 된 사용자만 view 조회 가능

    def post(self, request):
        usertype = request.data.get('usertype', '')
        email = request.data.get('email', '')
        password = request.data.get('password', '')
        password = make_password(password, salt=None, hasher='default')

        user = authenticate(request, email=email, password=password)
        if not user:
            UserModel(  )

            return Response({"message": "회원가입 성공!"})


