from django.db import models


status_choices = [
    ("exists", "exists"),
    ("non_existent", "non_existent")
]


class ProductManager(models.Manager):
    def is_available(self):
        return self.filter(status="exists")

    def is_not_available(self):
        return self.filter(status="non_existent")


class Product(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    color = models.CharField(max_length=50)
    status = models.CharField(choices=status_choices, max_length=12)
    p_manager = ProductManager()

    def __str__(self):
        return self.name
