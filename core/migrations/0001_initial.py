# Generated by Django 3.2.12 on 2023-02-10 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FlexibleDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Year')),
                ('month', models.IntegerField(blank=True, null=True, verbose_name='Month')),
                ('day', models.IntegerField(blank=True, null=True, verbose_name='Day')),
            ],
        ),
    ]