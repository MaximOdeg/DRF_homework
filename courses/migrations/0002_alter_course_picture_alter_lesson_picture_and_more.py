# Generated by Django 5.1.3 on 2024-11-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="course",
            name="picture",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/",
                verbose_name="превью(картинка)",
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="picture",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="images/",
                verbose_name="превью(картинка)",
            ),
        ),
        migrations.AlterField(
            model_name="lesson",
            name="video_link",
            field=models.URLField(blank=True, null=True),
        ),
    ]
