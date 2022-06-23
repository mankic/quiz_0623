from rest_framework import serializers

# from user.models import User as UserModel
from item.models import Category as  CategoryModel
from item.models import Item as  ItemModel
from item.models import Order as  OrderModel
from item.models import ItemOrder as  ItemOrderModel


class CategorySerializer(serializers.ModelSerializer):
               
    class Meta:
        model = CategoryModel
        fields = ['name']


class ItemSerializer(serializers.ModelSerializer):
               
    class Meta:
        model = ItemModel
        fields = ['name','category','image_url']


class OrderSerializer(serializers.ModelSerializer):
               
    class Meta:
        model = OrderModel
        fields = ['delivery_address', 'order_date','item']


class ItemOderSerializer(serializers.ModelSerializer):
               
    class Meta:
        model = ItemOrderModel
        fields = ['order','item','item_count']