# Generated by Django 4.2.10 on 2024-02-29 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0015_alter_tickets_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='solution',
            field=models.TextField(default=None),
        ),
    ]