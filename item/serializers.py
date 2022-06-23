from rest_framework import serializers

# from user.models import User as UserModel
from item.models import Category as CategoryModel
from item.models import Item as ItemModel
from item.models import Order as OrderModel
from item.models import ItemOrder as ItemOrderModel


class CategorySerializer(serializers.ModelSerializer):
                
    class Meta:
        model = CategoryModel
        fields = ["name"]


class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    # category = serializers.SerializerMethodField()
    # def get_category(self, obj):
    #     categories = obj.category.name
    #     return categories

    def create(self, validated_data):
        # validated_data = {
        #   'name' : 'cheeze pizza',
        #   'category' : {
        #       'name' : 'pizza'
        #   }
        # }
        category_data = validated_data.pop('category') # {'name':'pizza'}
        category_name = category_data.get('name')   # pizza
        category_obj = CategoryModel.objects.get(name=category_name)    # object
        
        item = ItemModel(category=category_obj, **validated_data)
        item.save()
        return item

    class Meta:
        model = ItemModel
        fields = ["name","category","image_url","category_id"]


class OrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer(many=True)
    class Meta:
        model = OrderModel
        fields = ["delivery_address","order_date","item"]


class ItemOrderSerializer(serializers.ModelSerializer):
                
    class Meta:
        model = ItemOrderModel
        fields = ["order","item","item_count"]