# Generated by Django 4.2.7 on 2024-01-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0012_alter_additionalindexedat_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="journal",
            name="ftp",
            field=models.CharField(
                blank=True, max_length=3, null=True, verbose_name="Ftp"
            ),
        ),
    ]
