from rest_framework import serializers, status
from .models import Address, UserProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from collections import OrderedDict

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
	def validate(self, attrs):
		try:
			username = User.objects.get(email=attrs['username']).username
			attrs['username'] = username
		except:
			username = attrs['username']
		user = authenticate(username=username, password=attrs['password'])
		if user is not None:
			if user.is_active: 
				data = super().validate(attrs)
				data = {}
				refresh = self.get_token(self.user)
				refresh['username'] = self.user.username
				try:
					obj = UserProfile.objects.get(user=self.user)
					data["refresh"] = str(refresh)
					data["access"] = str(refresh.access_token)
					data['first_name']= self.user.first_name
				except Exception as e:
					raise serializers.ValidationError('User verification failed!')
				return data
			else:
				raise serializers.ValidationError('Account is Blocked')
		else:
			raise serializers.ValidationError('Incorrect userid/email and password combination!')