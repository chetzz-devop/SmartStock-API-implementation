from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Inventory(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=400)
    current_stock = models.IntegerField()
    reorder_stock = models.IntegerField()

    def __str__(self):
        return self.item_name
