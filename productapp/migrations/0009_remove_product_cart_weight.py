# Generated by Django 5.0.6 on 2024-05-19 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0008_product_cart_brand_product_cart_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_cart',
            name='weight',
        ),
    ]
