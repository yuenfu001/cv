# Generated by Django 4.0 on 2021-12-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='name',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='name',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]