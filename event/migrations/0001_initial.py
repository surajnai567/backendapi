# Generated by Django 3.1.1 on 2021-05-10 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0006_auto_20210510_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField()),
                ('title', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('location', models.CharField(max_length=300)),
                ('is_private', models.CharField(max_length=6)),
                ('start_date', models.CharField(max_length=12)),
                ('end_date', models.CharField(max_length=12)),
                ('capacity', models.CharField(max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]