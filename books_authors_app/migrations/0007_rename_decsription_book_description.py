# Generated by Django 3.2.7 on 2021-10-13 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0006_alter_author_notes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='decsription',
            new_name='description',
        ),
    ]
