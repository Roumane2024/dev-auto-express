# Generated by Django 5.0.4 on 2024-06-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0005_alter_location_date_debut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='total_jours',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='', max_length=50),
        ),
    ]
