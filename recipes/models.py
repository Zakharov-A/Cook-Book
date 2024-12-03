from django.db import models
from django.utils import timezone

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Recipe(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    cooking_time = models.PositiveIntegerField()
    ingredients = models.TextField()
    number_of_servings = models.PositiveIntegerField()
    cooking_process = models.TextField()
    reviews_qty = models.IntegerField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="recipe" 
        )
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

