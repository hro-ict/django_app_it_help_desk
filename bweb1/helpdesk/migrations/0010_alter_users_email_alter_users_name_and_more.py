# Generated by Django 4.2.10 on 2024-02-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0009_remove_tickets_user_alter_tickets_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.TextField(max_length=50),
        ),
    ]