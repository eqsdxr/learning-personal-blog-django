# Generated by Django 3.2.19 on 2024-11-02 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='note',
            name='tags',
        ),
    ]
