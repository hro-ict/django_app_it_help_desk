# Generated by Django 4.2.10 on 2024-02-28 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0008_tickets_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='user',
        ),
        migrations.AlterField(
            model_name='tickets',
            name='user_email',
            field=models.TextField(default=''),
        ),
    ]
