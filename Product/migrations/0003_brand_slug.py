# Generated by Django 4.1.5 on 2023-02-09 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_product_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
