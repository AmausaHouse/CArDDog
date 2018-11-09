from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here

class loginview(APIView):
    def get(self, requeset):
        return Response(requeset.user.username)
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response('success')
        else:
            return Response('faild')
    def delete(self, request):
        logout(request)
        return Response('success')
class signupview(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        if User.objects.filter(username=username).exists():
            return Response(username + 'は取得されています')
        else:
            user = User.objects.create_user(username, password=password)
            login(request, user)
            return Response('success')