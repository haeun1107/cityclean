from django.db import models
from user.models import User
from trashcan.models import TrashCans

class Declaration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trashCans = models.ForeignKey(TrashCans, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)