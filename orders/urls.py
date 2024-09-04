from django.urls import path
from orders.models import Order

urlpatterns = [
    path('/users/<int:user_id>/orders', Order, name='order' )
]