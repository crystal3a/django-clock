# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 12:32


from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('shifts', '0003_shift_bool_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='key',
            field=models.CharField(blank=True, choices=[('S', 'Sick'), ('V', 'Vacation')], max_length=2,
                                   verbose_name='Key'),
        ),
    ]
