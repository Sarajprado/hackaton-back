from django.urls import path
from signin.views import SigninView

urlpatterns = [
    path('/users/signin', SigninView, name='login'),
]

