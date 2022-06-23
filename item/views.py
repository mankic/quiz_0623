from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category as CategoryModel
from .models import Item as ItemModel
from .models import Order as OrderModel
from .models import ItemOrder as ItemOrderModel

from .serializers import CategorySerializer
from .serializers import ItemSerializer
from .serializers import OrderSerializer
from .serializers import ItemOrderSerializer

from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models.query_utils import Q
# Create your views here.

class ItemView(APIView):

    def get(self, request):
        # category = request.GET.get('category', None)
        category = request.GET['category']  # appliance

        # items = ItemModel.objects.filter(category__name=category)
        category = CategoryModel.objects.get(name=category) # object(2)
        items = ItemModel.objects.filter(category_id=category)
        
        if items.exists():
            item_serializer = ItemSerializer(items, many=True).data
            return Response(item_serializer)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    
    def post(self, request):
        # item = request.data
        # print(request.data)
        item_serializer = ItemSerializer(data=request.data)
        if item_serializer.is_valid():
            item_serializer.save()
            return Response(item_serializer.data, status=status.HTTP_200_OK)
        return Response(item_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class OrderView(APIView):

    def get(self, request):
        order_id = request.GET['order_id']
        
        time = timezone.now() - timedelta(days=1)
        query = Q(id=order_id)|Q(order_date__gte=time)

        order_objs = OrderModel.objects.filter(query)
        return Response(OrderSerializer(order_objs, many=True).data)