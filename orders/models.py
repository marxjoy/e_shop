from datetime import datetime, timedelta

from django.conf import settings
from django.db import models

from shop.models import Product


def get_deadline():
    """
    Gets now date and time.
    :return: timedelta 7 days from now
    """
    return datetime.today() + timedelta(days=7)


class Order(models.Model):
    """
    Order model related to User model
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    deadline = models.DateField(default=get_deadline)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        # refactor
        return sum(item.get_cost() for item in self.items.all())



class OrderItem(models.Model):
    """
    Single item related to Order
    """
    order = models.ForeignKey(Order, related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.id

    def get_cost(self):
        return self.price * self.quantity


