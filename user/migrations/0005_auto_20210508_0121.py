# Generated by Django 3.1.1 on 2021-05-07 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210508_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default='f6ba292eed1c645f9c33', editable=False, max_length=20),
        ),
    ]
