# Generated by Django 4.0.1 on 2022-08-08 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinefood', '0011_remove_cartitems_itemtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitems',
            name='itemtitle',
            field=models.CharField(default='x', max_length=50),
        ),
    ]
