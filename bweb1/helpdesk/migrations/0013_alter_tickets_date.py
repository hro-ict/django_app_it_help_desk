# Generated by Django 4.2.10 on 2024-02-29 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0012_remove_tickets_user_tickets_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='date',
            field=models.DateField(auto_created=True),
        ),
    ]