# Generated by Django 4.2.7 on 2023-12-07 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("location", "0001_initial"),
        ("institution", "0003_institutionidentification"),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name="institution",
            name="institution_name_955317_idx",
        ),
        migrations.RemoveIndex(
            model_name="institution",
            name="institution_acronym_bacdf0_idx",
        ),
        migrations.AddField(
            model_name="institution",
            name="institution_identification",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="institution.institutionidentification",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="copyrightholder",
            unique_together={("institution",)},
        ),
        migrations.AlterUniqueTogether(
            name="editorialmanager",
            unique_together={("institution",)},
        ),
        migrations.AlterUniqueTogether(
            name="institution",
            unique_together={
                (
                    "institution_identification",
                    "level_1",
                    "level_2",
                    "level_3",
                    "location",
                )
            },
        ),
        migrations.AlterUniqueTogether(
            name="owner",
            unique_together={("institution",)},
        ),
        migrations.AlterUniqueTogether(
            name="publisher",
            unique_together={("institution",)},
        ),
        migrations.AlterUniqueTogether(
            name="sponsor",
            unique_together={("institution",)},
        ),
        migrations.RemoveField(
            model_name="institution",
            name="acronym",
        ),
        migrations.RemoveField(
            model_name="institution",
            name="is_official",
        ),
        migrations.RemoveField(
            model_name="institution",
            name="name",
        ),
        migrations.RemoveField(
            model_name="institution",
            name="official",
        ),
    ]
