# Generated by Django 4.2.10 on 2024-02-29 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0020_alter_tickets_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tickets',
            old_name='user_email',
            new_name='user_id',
        ),
    ]
