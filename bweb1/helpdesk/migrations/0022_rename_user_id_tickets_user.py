# Generated by Django 4.2.10 on 2024-02-29 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0021_rename_user_email_tickets_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tickets',
            old_name='user_id',
            new_name='user',
        ),
    ]
