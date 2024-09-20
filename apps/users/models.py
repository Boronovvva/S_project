from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from datetime import date

phone_regex = RegexValidator(
    regex=r'^\+996\d{9}$',
    message="Номер телефона должен быть в формате: '+996XXXXXXXXX'"
)

class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(
        max_length=255,
        verbose_name="Номер телефона",
        validators=[phone_regex],  
        unique=True, 
        blank=False,  
    )

    def __str__(self):
        return self.username

    @property
    def age(self):
        if self.date_of_birth:
            today = date.today()
            age = today.year - self.date_of_birth.year
            if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
                age -= 1
            return age
        return None

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
