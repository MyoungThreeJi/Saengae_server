# Generated by Django 3.2.6 on 2021-08-21 11:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detection', models.FloatField()),
            ],
            options={
                'db_table': 'detection',
                'ordering': ['-pad'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('enName', models.CharField(max_length=50)),
                ('average', models.FloatField()),
                ('max', models.FloatField()),
                ('min', models.FloatField()),
                ('sideEffect', models.TextField()),
            ],
            options={
                'db_table': 'ingredient',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Pad',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=300)),
                ('ingredients', models.ManyToManyField(through='Saengae_server.Detection', to='Saengae_server.Ingredient')),
            ],
            options={
                'db_table': 'pad',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star1', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('star2', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('star3', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('star4', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('content', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
                ('pad', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Saengae_server.pad')),
            ],
            options={
                'db_table': 'review',
                'ordering': ['-pad'],
            },
        ),
        migrations.AddField(
            model_name='detection',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Saengae_server.ingredient'),
        ),
        migrations.AddField(
            model_name='detection',
            name='pad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Saengae_server.pad'),
        ),
    ]
