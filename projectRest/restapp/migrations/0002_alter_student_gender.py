# Generated by Django 4.1.1 on 2022-09-05 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=5, null=True),
        ),
    ]
