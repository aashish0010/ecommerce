# Generated by Django 3.1.7 on 2021-03-05 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_remove_order_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]
