# Generated by Django 4.2.1 on 2023-05-30 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_product_created_product_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]