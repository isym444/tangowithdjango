# Generated by Django 5.0.3 on 2024-03-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rango", "0004_alter_category_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="slug",
            field=models.SlugField(default=""),
            preserve_default=False,
        ),
    ]
