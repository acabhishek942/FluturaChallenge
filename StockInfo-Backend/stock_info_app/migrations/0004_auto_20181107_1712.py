# Generated by Django 2.1.3 on 2018-11-07 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_info_app', '0003_auto_20181103_1040'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='closing_price',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='stock',
            name='opening_price',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
