# Generated by Django 4.2.10 on 2024-02-25 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0003_remove_tickets_state_tickets_is_open'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('mail', models.TextField()),
                ('password', models.TextField()),
                ('role', models.TextField()),
            ],
        ),
    ]