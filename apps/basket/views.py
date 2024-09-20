from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from apps.basket.models import Basket, BasketItem
from apps.basket.serializers import BasketSerializer,BasketItemSerializer

class BasketViewSet(ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

class BasketDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    
class BasketItemViewSet(ListCreateAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

class BasketItemDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
