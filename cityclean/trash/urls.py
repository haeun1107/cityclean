from django.urls import path
from .views import TrashCreateView, TrashsView, TrashListView, DeletetrashView

urlpatterns = [
    path('create/', TrashCreateView.as_view(), name='create-trash'),
    path('trashs/', TrashsView.as_view(), name='trashs-list'),
    path('list/', TrashListView.as_view(), name='trash-list-mark'),
    path('delete/<int:pk>/', DeletetrashView.as_view(), name='trash-delete'),
]