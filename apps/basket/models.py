from django.db import models
from django.contrib.auth import get_user_model

from apps.clock.models import clock

User = get_user_model()

# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="user_cart",
        verbose_name="Пользователь",
        blank=True, null=True, unique=True
    )
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )

    def __str__(self):
        return f"{self.user} {self.created}"
    
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"

class BasketItem(models.Model):
    basket = models.ForeignKey(
        Basket, on_delete=models.CASCADE,
        related_name="basket_items",
        verbose_name="Корзина"
    )
    clock = models.ForeignKey(
        clock, on_delete=models.CASCADE,
        related_name="clock_basket_items",
        verbose_name="Товар"
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Количество"
    )

    def __str__(self):
        return f"{self.basket} {self.clock} {self.quantity}"
    
    class Meta:
        verbose_name = "Товар в корзине"
        verbose_name_plural = "Товары в корзинах"