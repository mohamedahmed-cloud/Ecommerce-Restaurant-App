from rest_framework.views import APIView

from rest_framework import viewsets
from rest_framework.response import Response

from .models import Campaign, Category, ProductImage, Restaurant, Discount, Product
from .serializers import CampaignSerializer, CategorySerializer, DiscountSerializer, ProductImageSerializer, ProductSerializer, RestaurantSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self, serializer):
        serializer.save()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class=RestaurantSerializer

class CampaignViewSet(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer


from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Restaurant

from rest_framework.pagination import PageNumberPagination
class MyPaginationClass(PageNumberPagination):
    page_size = 2  # Number of items per page
    page_size_query_param = 'page_size'  # Custom query parameter to override page_size
    max_page_size = 100  
class index(APIView):
    pagination_class = MyPaginationClass
    
    def get(self, request):

        paginator = self.pagination_class()

        restaurants = Restaurant.objects.all()
        campaigns = Campaign.objects.all()
        categorys = Category.objects.all()
        products = Product.objects.all()

        
        # restaurants_paginated_queryset = paginator.paginate_queryset(restaurants, request)
        products_paginated_queryset = paginator.paginate_queryset(products, request)

        serializer = RestaurantSerializer(restaurants, many=True)
        serializer_campaign = CampaignSerializer(campaigns, many=True)
        serializer_categorys = CategorySerializer(categorys, many=True)
        serializer_products = ProductSerializer(products_paginated_queryset, many=True)

        return Response({'restaurants': serializer.data, 
                         'campaigns': serializer_campaign.data, 
                         'category': serializer_categorys.data,
                         'products': serializer_products.data,
                         
                         })