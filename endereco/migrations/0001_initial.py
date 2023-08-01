# Generated by Django 4.1.7 on 2023-07-04 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha1', models.CharField(max_length=255)),
                ('linha2', models.CharField(blank=True, max_length=255, null=True)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('latitude', models.IntegerField(blank=True, null=True)),
                ('longitude', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
