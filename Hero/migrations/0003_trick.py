# Generated by Django 3.0.1 on 2020-06-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hero', '0002_auto_20200613_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
