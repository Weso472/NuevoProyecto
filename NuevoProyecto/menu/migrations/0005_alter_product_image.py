# Generated by Django 4.2.1 on 2023-06-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='menu_photos'),
        ),
    ]
