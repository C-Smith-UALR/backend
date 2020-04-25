from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Physician


class PhysicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physician
        fields = ['id', 'firstName', 'lastName', 'maxShiftLoad', 'phoneNumber', 'specialty']

class PhysicianMiniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Physician
        fields = ['id', 'lastName']
