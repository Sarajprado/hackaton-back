from django.db import models
from users.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=100, default='Pendente')

    def __str__(self):
        return f'Order {self.id} for {self.user}'

