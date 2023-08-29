# Generated by Django 3.2.18 on 2023-07-06 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Название')),
                ('code', models.CharField(max_length=10, verbose_name='Код')),
                ('wight', models.IntegerField(verbose_name='Вес')),
            ],
            options={
                'verbose_name': 'Упаковка',
                'verbose_name_plural': 'Упаковки',
            },
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=10, verbose_name='Код города отправителя')),
                ('receiver', models.CharField(max_length=10, verbose_name='Код города получателя')),
            ],
            options={
                'verbose_name': 'Маршрут',
                'verbose_name_plural': 'Маршруты',
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered', models.IntegerField(verbose_name='Доставлено')),
                ('rejection', models.IntegerField(verbose_name='Отказ')),
                ('amount', models.IntegerField(verbose_name='Сумма')),
                ('date', models.DateField(verbose_name='Дата')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistic', to='statistic.package')),
                ('partner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistic', to='partner.partner')),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='statistic', to='statistic.route')),
            ],
            options={
                'verbose_name': 'Статистика',
                'verbose_name_plural': 'Статистики',
            },
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['date'], name='statistic_s_date_30cfa5_idx'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['date', 'partner'], name='statistic_s_date_75c6f5_idx'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['date', 'route'], name='statistic_s_date_7f557a_idx'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['date', 'package'], name='statistic_s_date_903733_idx'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['date', 'partner', 'route'], name='statistic_s_date_00ddcd_idx'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['date', 'partner', 'package'], name='statistic_s_date_64a2fc_idx'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['date', 'route', 'package'], name='statistic_s_date_500d66_idx'),
        ),
        migrations.AddIndex(
            model_name='statistic',
            index=models.Index(fields=['date', 'partner', 'route', 'package'], name='statistic_s_date_f7c7e0_idx'),
        ),
    ]