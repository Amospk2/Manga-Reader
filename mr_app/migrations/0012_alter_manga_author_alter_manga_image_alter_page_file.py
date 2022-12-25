# Generated by Django 4.1.4 on 2022-12-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mr_app', '0011_alter_capitulo_release_date_alter_manga_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='author',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='manga',
            name='image',
            field=models.ImageField(default=None, upload_to='storage/manga/'),
        ),
        migrations.AlterField(
            model_name='page',
            name='file',
            field=models.ImageField(upload_to='storage/page/'),
        ),
    ]