# Generated by Django 2.0.5 on 2018-07-01 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20180701_0258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_content',
            name='Cart_contentID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
