from django.db import models
from django.contrib.auth.models import AbstractUser

# User 모델을 확장하기위해 AbstractUser 상속
class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "male")
        FEMAIL = ("femail", "female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")
    
    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"

        
    # 원하는 양식의 필드를 정의
    first_name = models.CharField(max_length=150, editable=False,)
    last_name = models.CharField(max_length=150, editable=False,)
    name = models.CharField(max_length=150, default='')
    avatar = models.ImageField(blank=True)
    is_host = models.BooleanField(default=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices,)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices,)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices,)
