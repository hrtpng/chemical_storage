# Generated by Django 4.1.7 on 2023-02-25 18:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("storage", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="compound",
            old_name="place",
            new_name="rack",
        ),
        migrations.AddField(
            model_name="compound",
            name="shelf",
            field=models.CharField(default="", max_length=10),
            preserve_default=False,
        ),
    ]