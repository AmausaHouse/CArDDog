from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import os
import uuid
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../CArDCat'))
import imagepredict
from keras import backend as K
# Create your views here

class loginview(APIView):
    def get(self, requeset):
        return Response(requeset.user.username)
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
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
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return Response('success')
class findface(APIView):
    def post(self, requeset):
        """
        UPLOADE_DIR = '/src/files/faceimages'
        file = requeset.FILES['file']
        filename = str(uuid.uuid4()) + '.jpg'
        path = UPLOADE_DIR + '/' + filename
        destination = open(path, 'wb')
        for chunk in file.chunks():
            destination.write(chunk)
        K.clear_session()
        p = imagepredict.ImagePredictor()
        # print(p.predict(path))
        return Response(p.predict(path))
        """
        a, base64encdjpg = requeset.data['file'].split(';base64,') 
        K.clear_session()
        p = imagepredict.ImagePredictor()
        return Response(p.predict_from_base64img(base64encdjpg))