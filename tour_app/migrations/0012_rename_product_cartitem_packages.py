# Generated by Django 4.2.6 on 2023-11-21 06:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tour_app", "0011_alter_packages_package_id_cartitem"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cartitem",
            old_name="product",
            new_name="packages",
        ),
    ]