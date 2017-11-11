# -*- coding: utf-8 -*-


from django.db import models, migrations
from django.conf import settings
import clock.contracts.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('department', models.CharField(max_length=200)),
                ('department_short', models.CharField(max_length=100, null=True, blank=True)),
                ('hours', clock.contracts.fields.WorkingHoursField()),
                ('contact', models.EmailField(max_length=254, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
