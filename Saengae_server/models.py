from django.db import models


# 생리대:성분 = 1:N 관계
class Ingredient(models.Model):
    # pad_name = models.ForeignKey(Pad, on_delete=models.CASCADE)
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    enName = models.CharField(max_length=20)
    sideEffect = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'ingredient'


class Pad(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=20)
    image = models.CharField(max_length=300)
    ingredients = models.ManyToManyField(Ingredient, through='Detection')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pad'


class Detection(models.Model):
    pad_id = models.ForeignKey(Pad, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    detection = models.FloatField()

    def __str__(self):
        return self.detection

    class Meta:
        db_table = 'detection'

