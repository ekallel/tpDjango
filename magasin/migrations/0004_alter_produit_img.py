# Generated by Django 4.1.7 on 2023-03-07 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("magasin", "0003_produit_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="produit",
            name="Img",
            field=models.ImageField(blank=True, null=True, upload_to="media/"),
        ),
    ]