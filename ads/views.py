from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from ads.models import Ad
from ads.serializers import AdCreateSerializer, AdListSerializer, AdSerializer


class AdView(RetrieveUpdateDestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdCreateView(CreateAPIView):
    serializer_class = AdCreateSerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdListSerializer