# Generated by Django 4.2.6 on 2023-11-21 07:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tour_app", "0013_rename_packages_cartitem_package"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartitem",
            old_name="package",
            new_name="packages",
        ),
    ]
