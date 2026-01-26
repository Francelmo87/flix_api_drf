from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from app.permissions import GlobalDefaultpermission
from .models import Review
from .serializers import ReviewSerializer


class ReviewListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultpermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultpermission,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
