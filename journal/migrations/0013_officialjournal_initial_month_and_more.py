# Generated by Django 4.1.10 on 2023-09-21 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("journal", "0012_alter_officialjournal_terminate_month"),
    ]

    operations = [
        migrations.AddField(
            model_name="officialjournal",
            name="initial_month",
            field=models.CharField(
                blank=True,
                choices=[
                    ("01", "January"),
                    ("02", "February"),
                    ("03", "March"),
                    ("04", "April"),
                    ("05", "May"),
                    ("06", "June"),
                    ("07", "July"),
                    ("08", "August"),
                    ("09", "September"),
                    ("10", "October"),
                    ("11", "November"),
                    ("12", "December"),
                ],
                max_length=2,
                null=True,
                verbose_name="Month Year",
            ),
        ),
        migrations.AddField(
            model_name="officialjournal",
            name="initial_year",
            field=models.CharField(
                blank=True, max_length=4, null=True, verbose_name="Initial Year"
            ),
        ),
    ]
