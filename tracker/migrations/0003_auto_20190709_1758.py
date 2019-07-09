# Generated by Django 2.2.3 on 2019-07-09 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20190708_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='tracker.Project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='url',
            field=models.CharField(max_length=50, unique=True, verbose_name='URL адреса'),
        ),
    ]