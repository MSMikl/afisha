# Generated by Django 4.0.6 on 2022-07-18 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_alter_image_place'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['order_number']},
        ),
        migrations.AlterField(
            model_name='image',
            name='order_number',
            field=models.IntegerField(default=0, verbose_name='Порядковый номер'),
        ),
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.ImageField(upload_to='', verbose_name='Картинка'),
        ),
    ]