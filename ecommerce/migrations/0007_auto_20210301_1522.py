# Generated by Django 3.1.7 on 2021-03-01 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_auto_20210301_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.DeleteModel(
            name='Cat',
        ),
    ]