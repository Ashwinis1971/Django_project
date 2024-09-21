from django.db import models
from customers.models import Customer
from products.models import Product

# data model for order
class Order(models.Model):
    LIVE=1
    DElETE=0
    DELETE_CHOICES=((LIVE, 'LIVE'), (DElETE, 'DELETE'))
    
    CART_STAGE=0
    ORDER_CONFIRMED=1
    ORDER_PROCESSED=2
    ORDER_DELIVERED=3
    ORDER_REJECTED=4
    
    STATUS_CHOICE=((ORDER_PROCESSED, 'ORDER_PROCESSED'),
                   (ORDER_DELIVERED, 'ORDER_DELIVERED'), 
                   (ORDER_REJECTED, 'ORDER_REJECTED'))
    
    order_status=models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    owner=models.ForeignKey(Customer, on_delete=models.SET_NULL,
                            related_name='orders', null=True)
    delete_status=models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateField(auto_now=True)


# models for OrderedItem
class OrderedItem(models.Model):
    product=models.ForeignKey(Product, related_name='add_carts', 
                              on_delete=models.SET_NULL, null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(Order, on_delete=models.CASCADE, 
                            related_name='added_items')
    
    