# Generated by Django 3.2.5 on 2021-09-01 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=10000)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.URLField()),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
