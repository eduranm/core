# Generated by Django 4.1.10 on 2023-10-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("article", "0005_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articlefunding",
            name="award_id",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Award ID"
            ),
        ),
    ]
