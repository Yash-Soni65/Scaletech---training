from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateView(APIView):
    def get(self, request):
        cached_products = cache.get('products')
        if cached_products is not None:
            return Response(cached_products)
        print("Cache miss: Fetching products from the database.")
        print("Fetching products from the database.")
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        cache.set('products', serializer.data, timeout=60)  
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
