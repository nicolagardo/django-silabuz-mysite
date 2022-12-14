# Generated by Django 4.1.3 on 2022-11-29 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("escuela", "0002_profesor"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profesor",
            options={"verbose_name_plural": "profesores"},
        ),
        migrations.AlterModelOptions(
            name="salon",
            options={"verbose_name_plural": "salones"},
        ),
        migrations.AddField(
            model_name="salon",
            name="idProfesor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="escuela.profesor",
            ),
        ),
    ]
