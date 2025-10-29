from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name