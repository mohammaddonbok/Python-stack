# Generated by Django 2.2.4 on 2020-12-14 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
