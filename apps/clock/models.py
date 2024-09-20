from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class clock(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_clock',
        verbose_name="Пользователь"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="image/",
        verbose_name="Логотип"
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новое поступление'
        verbose_name_plural = 'Новые поступления'