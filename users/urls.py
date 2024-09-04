from django.urls import path
from users.views import user

urlpatterns = [
    path('/user/signup', user, name='signup'),
    path('/users', user, name='user')
]

