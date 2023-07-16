from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets,permissions

from backend.products.models import Product
from .models import DeliveryCharge, Order, OrderItem
from .serializers import DeliveryChargeSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.response import Response
from rest_framework import status




class DeliveryChargeViewSet(viewsets.ModelViewSet):
    queryset = DeliveryCharge.objects.all()
    serializer_class = DeliveryChargeSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        elif self.request.method == 'GET':
            return [permissions.IsAuthenticated()]
        else:
            return super().get_permissions()


def calculate_delivery_total_price(order_items_data):
    total_price = 0
    for item_data in order_items_data:
        item_quantity = item_data.get('quantity', 1)
        item_price=  Product.objects.get_price(item_data['product'])
        total_price+=item_price *item_quantity
    return total_price


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        order_data = request.data
        order_items_data = order_data.pop('order_items', [])
        serializer = self.get_serializer(data=order_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        order = serializer.instance
        order_items = []
        for item_data in order_items_data:
            item_data['order'] = order.id
            order_item_serializer = OrderItemSerializer(data=item_data)
            order_item_serializer.is_valid(raise_exception=True)
            order_item_serializer.save()
            order_items.append(order_item_serializer.data)

        calculate_delivery_total_price(order_items_data)
        
        headers = self.get_success_headers(serializer.data)
        return Response(
            {
                'order': serializer.data,
                'order_items': order_items
            },
            status=status.HTTP_201_CREATED,
            headers=headers
        )

