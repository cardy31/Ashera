# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 15:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=25)),
                ('field', models.CharField(max_length=256)),
                ('temp', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('humidity', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('nitrate', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('phosphorus', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('potassium', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('pH', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('light', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('envTemp', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('envHumidity', models.DecimalField(decimal_places=3, max_digits=10, null=True)),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fields', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
