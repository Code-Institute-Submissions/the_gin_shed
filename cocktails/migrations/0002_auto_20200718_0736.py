# Generated by Django 3.0.7 on 2020-07-18 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktailrecipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
