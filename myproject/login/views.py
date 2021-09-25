from django.shortcuts import render
from .models import UserProfile, Address
from . serializers import MyTokenObtainPairSerializer
from rest_framework import generics, permissions, serializers, status
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import FormParser, MultiPartParser


class LoginView(TokenObtainPairView):
	"""
	Login View with jWt token authentication
	"""
	serializer_class = MyTokenObtainPairSerializer

