# Generated by Django 4.0 on 2021-12-12 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0004_rename_chat_chatdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatdata',
            name='date',
        ),
    ]
