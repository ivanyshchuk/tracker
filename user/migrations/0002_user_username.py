# Generated by Django 2.2.3 on 2019-07-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='username'),
        ),
    ]
