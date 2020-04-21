# Generated by Django 2.2.10 on 2020-04-21 22:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_auto_20200421_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=240, verbose_name='Description')),
                ('completed', models.BooleanField(verbose_name='Completed')),
            ],
        ),
    ]
