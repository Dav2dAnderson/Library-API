from django.shortcuts import render

from rest_framework import permissions
from rest_framework import generics

from .models import Customer

from .serializers import CustomerSerializer
# Create your views here.


class CustomerListView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAdminUser, ]


