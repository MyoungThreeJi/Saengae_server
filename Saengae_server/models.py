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
    pad_id = models.ForeignKey(Pad, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    detection = models.FloatField()

    class Meta:
        db_table = 'detection'
        ordering = ['-pad_id']


