# Generated by Django 4.1.4 on 2022-12-22 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mr_app', '0014_alter_manga_image_alter_page_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='capitulo',
            old_name='fk_manga',
            new_name='manga',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='fk_page',
            new_name='page',
        ),
        migrations.RenameField(
            model_name='forumpostcomment',
            old_name='fk_forumpost',
            new_name='forumpost',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='fk_capitulo',
            new_name='capitulo',
        ),
    ]
