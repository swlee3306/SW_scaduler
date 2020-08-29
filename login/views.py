from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.Response import Response
from .models import LoginUser
# Create your views here.


class RegistUser(APIView):
    def post(self, request):
        user_id = request.data.get('user_id')
        user_pw = request.data.get('user_pw')

        LoginUser.objects.create(user_id=user_id, user_pw=user_pw)

        data = dict{
            user_id = user_id,
            user_pw = user_pw

        }

        return Response(data)


