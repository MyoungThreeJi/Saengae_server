import csv
import os
import django
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from Saengae_server.models import *


# 현재 디렉토리 경로 표시
os.chdir(".")
print("Current dir=", end=""), print(os.getcwd())

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print("BASE_DIR=", end=""), print(BASE_DIR)

sys.path.append(BASE_DIR)

# 프로젝트명.settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

# csv 파일 경로
CSV_PATH_1 = 'pad_info.csv'
CSV_PATH_2 = 'ingredient_info.csv'
CSV_PATH_3 = 'pad_ingredient.csv'


# Pad
with open(CSV_PATH_1, newline='', encoding='utf-8-sig') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        # print(row)
        Pad.objects.create(
            id=row['pad_id'],
            manufacturer=row['manufacturer'],
            name=row['name'],
            image=row['image'],
            safeScore=row['safety_score'],
            rank=row['rank'],
        )

# Ingredient
with open(CSV_PATH_2, newline='', encoding='utf-8-sig') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        # print(row)
        Ingredient.objects.create(
            id=row['ingredient_id'],
            name=row['name'],
            enName=row['en_name'],
            average=row['average'],
            max=row['max'],
            min=row['min'],
            sideEffect=row['side_effect'],
        )

# Detection
with open(CSV_PATH_3, newline='', encoding='CP949') as csvfile:
    data_reader = csv.DictReader(csvfile)

    for row in data_reader:
        # print(row)
        padId = Pad.objects.get(id=row['pad_id'])
        ingredientId = Ingredient.objects.get(id=row['ingredient_id'])
        Detection.objects.create(
            pad=padId,
            ingredient=ingredientId,
            detection=row['detection'],
        )

