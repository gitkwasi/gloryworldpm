# Generated by Django 4.2.1 on 2023-05-23 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_ticket_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['-date_created']},
        ),
    ]
