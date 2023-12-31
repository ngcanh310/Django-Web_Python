# Generated by Django 4.2.5 on 2023-10-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_delete_food_delete_tour'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idFood', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('rate', models.FloatField()),
                ('duration', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idTour', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('rate', models.FloatField()),
                ('duration', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
        ),
    ]
