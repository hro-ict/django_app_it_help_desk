# Generated by Django 4.2.10 on 2024-02-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0016_alter_tickets_solution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='date',
            field=models.TextField(default=None),
        ),
    ]