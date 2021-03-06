# Generated by Django 3.1.1 on 2021-05-20 17:46

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20210520_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='events',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='followers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='following',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default='def133677f6119e8ea9f', editable=False, max_length=20),
        ),
    ]
