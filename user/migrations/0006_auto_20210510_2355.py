# Generated by Django 3.1.1 on 2021-05-10 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210508_0121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(default='b44cfb2ab8370e116244', editable=False, max_length=20),
        ),
    ]
