# Generated by Django 4.0 on 2021-12-19 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='please your first name is actually your own name', max_length=50)),
                ('last_name', models.CharField(help_text='please your last name is actually your surname name', max_length=50)),
                ('summary', models.TextField(help_text='Tell us all little about yourself', null=True)),
                ('date_of_birth', models.DateField()),
                ('date_created', models.DateField(auto_now=True)),
                ('date_updated', models.DateField(auto_now_add=True)),
                ('state_of_origin', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='soo', to='resume.state')),
            ],
        ),
    ]
