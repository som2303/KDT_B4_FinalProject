# Generated by Django 4.0.3 on 2023-01-11 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('b4', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
