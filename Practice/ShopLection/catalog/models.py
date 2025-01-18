from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # Название категории, unique=True гарантирует, что названия категорий не повторяются.

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200) # Название товара
    description = models.TextField(blank=True) # Описание товара (опционально)
    price = models.DecimalField(max_digits=10, decimal_places=2) # Цена товара
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # Связь с категорией, on_delete=models.CASCADE означает, что удаление категории удалит связанные товары.
    created_at = models.DateTimeField(auto_now_add=True) # Дата добавления товара

    def __str__(self):
        return self.name

