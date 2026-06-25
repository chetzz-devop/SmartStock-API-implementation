from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from rest_framework import serializers
from .models import Inventory


class InventorySerializers(serializers.ModelSerializer):
    supplier_name = serializers.CharField(
        source='supplier.name', read_only=True)
    alert = serializers.SerializerMethodField()

    class Meta:
        model = Inventory
        fields = ['alert', 'supplier_name', 'supplier', 'item_name', 'id',
                  'current_stock', 'reorder_stock']

    def get_alert(self, obj):
        if obj.current_stock <= obj.reorder_stock:
            return "RESTOCK REQUIRED"
        return "OK"

    def validate(self, data):
        name = data.get('item_name')
        current = data.get('current_stock')
        reorder = data.get('reorder_stock')
        finalstock = current+reorder
        if finalstock > 10:
            raise serializers.ValidationError(
                f"cannot book more than 10 Kg wait untill {name} is lesser  ")
        return data
