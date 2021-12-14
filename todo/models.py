from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.category_name


class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=500, blank=False)
    category = models.ManyToManyField(Category, related_name="category")

    PRIORITY_CHOICES = [
        ('high', 'high'),
        ('medium', 'medium'),
        ('low', 'low')
    ]
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default="low")
    create_time = models.DateField(auto_now_add=True)
    dead_line = models.DateField()

    STATUS_CHOICES = [
        ('todo', 'todo'),
        ('progress', 'progress'),
        ('done', 'done')
    ]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="todo")

    def __str__(self):
        return self.title

