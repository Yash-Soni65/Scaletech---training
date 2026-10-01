from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView, Response
from rest_framework.viewsets import ModelViewSet

from customer.serializers import CustomerSerializer
from .models import Customer
from rest_framework.permissions import IsAuthenticated

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
    
    
class CustomerListCreateView(APIView):
    def get(self,request):
        customers = Customer.objects.all()
        serializers = CustomerSerializer(customers, many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializers = CustomerSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=201)
        return Response(serializers.errors, status=400)

            
class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
    
# Create your views here.
