# Generated by Django 3.2.18 on 2023-07-06 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistic', '0004_alter_package_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='name',
            field=models.CharField(max_length=35, verbose_name='Название'),
        ),
    ]
