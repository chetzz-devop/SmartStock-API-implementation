from rest_framework.views import APIView
from django.db.models import F, Sum
from django.shortcuts import render
from .models import Inventory, Supplier
from rest_framework import generics
from .serializer import InventorySerializers
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.authentication import SessionAuthentication
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Inventory


class CreateInv(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializers
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['item_name']


class EditInv(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializers
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]


class ReorderListView(generics.ListAPIView):
    serializer_class = InventorySerializers
    authentication_classes = [JWTAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Inventory.objects.filter(current_stock__lte=F('reorder_stock'))


class SendOrderEmailView(APIView):
    def post(self, request, pk):
        try:
            item = Inventory.objects.get(pk=pk)
            supplier = item.supplier
            if item.current_stock > item.reorder_stock:
                return Response(
                    {"message": "Stock is healthy. No email needed."},
                    status=400
                )

            send_mail(
                subject=f"Restock Request: {item.item_name}",
                message=f"Hello {supplier.name},\n\nWe are low on stock for {item.item_name}. Please send us a new delivery as soon as possible.\n\nThank you,\nCafe Management",
                from_email='pikacafe@gmail.com',
                recipient_list=[supplier.email],
                fail_silently=False,
            )

            return Response({"message": f"Email sent to {supplier.email} for {item.item_name}"})

        except Inventory.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
