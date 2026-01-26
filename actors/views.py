from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultpermission
from .models import Actor
from .serializers import ActorSerializer


class ActorListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultpermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultpermission,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
