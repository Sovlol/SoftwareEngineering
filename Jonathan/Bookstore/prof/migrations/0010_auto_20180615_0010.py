# Generated by Django 2.0.5 on 2018-06-15 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0009_auto_20180614_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='AuthorID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prof.AUTHOR'),
        ),
    ]