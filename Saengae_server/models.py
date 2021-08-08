from django.db import models


# 생리대:성분 = 1:N 관계
class Pad(models.Model):
    manufacturer = models.CharField(max_length=10)
    name = models.CharField(max_length=30)
    image = models.URLField()

    class Meta:
        db_table = 'pad'


class Ingredient_info(models.Model):
    pad_name = models.ForeignKey(Pad, on_delete=models.CASCADE)
    igd_koName = models.CharField(max_length=20)
    igd_enName = models.CharField(max_length=20)
    igd_detection = models.FloatField()
    igd_sideEffect = models.TextField()

    class Meta:
        db_table = 'ingredient_information'

