# Generated by Django 2.0.5 on 2018-06-02 17:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('num_stars', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('instrument', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='AuthorID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.AUTHOR'),
        ),
        migrations.AlterField(
            model_name='book',
            name='GenreID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.GENRE'),
        ),
        migrations.AlterField(
            model_name='book',
            name='PublisherID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.PUBLISHER_INFO'),
        ),
        migrations.AlterField(
            model_name='book_rating',
            name='ISBN',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.BOOK'),
        ),
        migrations.AlterField(
            model_name='cart_content',
            name='Cart_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.CART'),
        ),
        migrations.AlterField(
            model_name='cart_content',
            name='ISBN',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.BOOK'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='ISBN',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.BOOK'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Time_posted',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.USER'),
        ),
        migrations.AlterField(
            model_name='preferred_credit_card',
            name='C_card_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.CREDIT_CARD'),
        ),
        migrations.AlterField(
            model_name='purchase_history_content',
            name='ISBN',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.BOOK'),
        ),
        migrations.AlterField(
            model_name='purchase_history_content',
            name='Username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.USER'),
        ),
        migrations.AlterField(
            model_name='rating_history',
            name='ISBN',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.BOOK'),
        ),
        migrations.AlterField(
            model_name='reserved_credit_card',
            name='C_card_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.CREDIT_CARD'),
        ),
        migrations.AlterField(
            model_name='reserved_credit_card',
            name='Username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.USER'),
        ),
        migrations.AlterField(
            model_name='saved_for_later_content',
            name='ISBN',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.BOOK'),
        ),
        migrations.AlterField(
            model_name='saved_for_later_content',
            name='Username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.USER'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Cart_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.CART'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Home_address_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.USER_HOME_ADDRESS'),
        ),
        migrations.AlterField(
            model_name='user',
            name='Preferred_credit_card_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.PREFERRED_CREDIT_CARD'),
        ),
        migrations.AlterField(
            model_name='user_home_address',
            name='Address_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.ADDRESS'),
        ),
        migrations.AlterField(
            model_name='user_shipping_address',
            name='Address_ID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.ADDRESS'),
        ),
        migrations.AlterField(
            model_name='user_shipping_address',
            name='Username',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.USER'),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Musician'),
        ),
    ]
