from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# 생리대:성분 = 1:N 관계

class Ingredient(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    enName = models.CharField(max_length=50)
    average = models.FloatField()
    max = models.FloatField()
    min = models.FloatField()
    sideEffect = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ingredient'
        ordering = ['-id']


class Pad(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    ingredients = models.ManyToManyField(Ingredient, through='Detection')
    # through_fields = ("pad_id", "ingredient_id"),  # (소스모델, 타겟모델) 순서

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pad'
        ordering = ['-id']


class Detection(models.Model):
    pad = models.ForeignKey(Pad, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    detection = models.FloatField()

    class Meta:
        db_table = 'detection'
        ordering = ['-pad']


class Review(models.Model):
    pad = models.ForeignKey(Pad, on_delete=models.CASCADE, blank=True)
    star1 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)]) # 착용감
    star2 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)]) # 흡수력
    star3 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)]) # 샘방지
    star4 = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)]) # 가성비
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'review'
        ordering = ['-pad']
