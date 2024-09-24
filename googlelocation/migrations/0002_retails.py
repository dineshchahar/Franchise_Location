# Generated by Django 5.1.1 on 2024-09-23 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlelocation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Retails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=300)),
                ('coordinates', models.TextField(max_length=300)),
                ('types', models.TextField(max_length=500)),
                ('rating', models.FloatField()),
                ('user_rating', models.FloatField()),
                ('Travel_Distance', models.FloatField()),
                ('Travel_Time', models.FloatField()),
            ],
        ),
    ]
