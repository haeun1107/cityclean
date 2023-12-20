from django.urls import path
from .views import TrashCanCreateView, TrashCanListView, TrashCansView

urlpatterns = [
    path('create/', TrashCanCreateView.as_view(), name='create-trashcan'),
    path('list/', TrashCanListView.as_view(), name='trashcan-list'),
    path('trash-cans/', TrashCansView.as_view(), name='trash-cans-list'),
]