from rest_framework import serializers

from apps.basket.models import Basket, BasketItem

class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('id','user','created')
        
class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = ('id','basket','clock','quantity')