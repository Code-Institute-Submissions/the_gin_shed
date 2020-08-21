# Generated by Django 3.0.7 on 2020-08-21 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='friendly_name',
            field=models.CharField(blank=True, default='', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, default='', max_length=1024),
            preserve_default=False,
        ),
    ]
