# Generated by Django 2.1.8 on 2019-10-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='picture',
            field=models.ImageField(upload_to='seller/imgs'),
        ),
    ]
