from django.db import models


class Collection(models.Model):
    title = models.CharField(max_length=255)


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT) # a one to many relationship 


ORDER_STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('canceled', 'Canceled')
    ]


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.PROTECT) 
    created_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=20, default='pending', choices=ORDER_STATUS_CHOICES)


class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE) # a one to many relationship between order and order item, if an order is deleted, all its items will be deleted as well
    product=models.ForeignKey(Product, on_delete=models.PROTECT) # a one to many relationship, if a product is deleted, the order item will not be deleted, but it will raise an error if we try to delete a product that is referenced by an order item
    quantity=models.PositiveSmallIntegerField() # allow only positive integers 
    unit_price=models.DecimalField(max_digits=10, decimal_places=2) 

class Customer(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)

class Cart(models.Model):
    customer=models.OneToOneField(Customer, on_delete=models.CASCADE, primary_key=True)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()
    class Meta:
        unique_together = ('cart', 'product') 
