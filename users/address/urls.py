from django.urls import path
from address.models import Address

urlpatterns = [
    path('/users/address', Address, name='address' ),
]

