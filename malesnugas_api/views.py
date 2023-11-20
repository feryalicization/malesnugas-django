from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status
from .filters import UsertFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics




def current_datetime(request):
    now = datetime.datetime.now()
    user = User.objects.all().filter(username='fery').first()
    print(user)
    html = f"<html><body>It is now %s.</body></html> <br> {user.full_name}" % now
    return HttpResponse(html)

class UserListAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UsertFilter

class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
