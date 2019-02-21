from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Profile
from social_django.models import UserSocialAuth

import os
import uuid
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../CArDCat'))
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
        a, base64encdjpg = requeset.data['file'].split(';base64,') 
        K.clear_session()
        p = imagepredict.ImagePredictor()
        return Response(p.predict_from_base64img(base64encdjpg))
        """
        return Response('工事中')
class profile(APIView):
    def post(self, request):
        req_type = request.query_params["req_type"]
        if req_type == "icon":
            user = request.user
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.user_icon_url = _get_icon_from_user(user)
            profile.save()
            return Response('success')
        elif req_type == "name":
            user = request.user
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.display_name = request.data["name"]
            profile.save()
            return Response('success')
        elif req_type == "dict":
            user = request.user
            profile, _ = Profile.objects.get_or_create(user=user)
            profile.user_dictionaly = request.data["dict"]
            profile.save()
            return Response('success')
        else:
            return Response('failed')
    def get(self, requeset):
        user = requeset.user
        profile, _ = Profile.objects.get_or_create(user=user)
        icon = profile.user_icon_url
        name = profile.display_name
        dict_d = profile.user_dictionaly
        return Response({"icon": icon, "name": name, "dict": dict_d})

def _get_icon_from_user(user):
    social_user = UserSocialAuth.objects.get(user=user)
    provider = social_user.provider
    if provider == "github":
        print(social_user.extra_data)
        return "https://github.com/{}.png".format(social_user.extra_data["login"])
    elif provider == "twitter":
        pass
    return ''
