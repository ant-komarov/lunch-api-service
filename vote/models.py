from django.contrib.auth import get_user_model
from django.db import models

from config import settings
from restaurant.models import Menu


class Vote(models.Model):
    date = models.DateField(auto_now_add=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date"]
        unique_together = ["date", "user"]

    def __str__(self):
        return f"{self.date}"
