# Generated by Django 2.2.16 on 2022-12-26 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Загрузите картинку', upload_to='posts/', verbose_name='Картинка'),
        ),
    ]
