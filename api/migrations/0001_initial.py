# Generated by Django 3.2.5 on 2021-09-01 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('rating', models.CharField(max_length=100)),
                ('imgback', models.URLField(max_length=100)),
                ('metacritic', models.FloatField()),
            ],
        ),
    ]
