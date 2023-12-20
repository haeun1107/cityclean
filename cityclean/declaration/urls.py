from django.urls import path
from .views import DeclarationView

urlpatterns = [
    path('', DeclarationView.as_view(), name='create-declaration'),
]