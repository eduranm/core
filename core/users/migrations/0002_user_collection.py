# Generated by Django 4.2.7 on 2024-01-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("collection", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="collection",
            field=models.ManyToManyField(
                blank=True, to="collection.collection", verbose_name="Collection"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="journal",
            field=models.ManyToManyField(
                blank=True, to="journal.journal", verbose_name="Journal"
            ),
        ),
    ]