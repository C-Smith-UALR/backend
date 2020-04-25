#largely obtained from Django REST quickstart: https://www.django-rest-framework.org/tutorial/quickstart/

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import PhysicianSerializer, PhysicianMiniSerializer
from .models import Physician
from rest_framework.response import Response


class PhysicianViewSet(viewsets.ModelViewSet):

    queryset = Physician.objects.all()
    serializer_class = PhysicianSerializer

    def list(self, request, *args, **kwargs):
        physicians = Physician.objects.all()
        serializer = PhysicianMiniSerializer(physicians, many=True)
        return Response(serializer.data)


