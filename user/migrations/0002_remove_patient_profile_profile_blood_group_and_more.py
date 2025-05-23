# Generated by Django 5.2.1 on 2025-05-10 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='blood_group',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='experience',
            field=models.PositiveIntegerField(blank=True, help_text='Years of experience', null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='hourly_rate',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='specialty',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
