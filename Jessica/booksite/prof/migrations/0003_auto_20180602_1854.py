# Generated by Django 2.0.5 on 2018-06-02 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prof', '0002_auto_20180602_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='AuthorID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='prof.AUTHOR'),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='CVV',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='Exp_day',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='Exp_month',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='credit_card',
            name='Exp_year',
            field=models.CharField(max_length=4),
        ),
    ]