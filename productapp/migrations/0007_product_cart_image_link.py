# Generated by Django 5.0.6 on 2024-05-19 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productapp', '0006_product_cart_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_cart',
            name='image_link',
            field=models.CharField(default='https://perfumesamples.in/cdn/shop/products/libre-by-yves-saint-laurent-sampledecants-673052_1200x.jpg?v=1699381687', max_length=500),
            preserve_default=False,
        ),
    ]