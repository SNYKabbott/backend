# Generated by Django 2.2.10 on 2020-04-21 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_remove_children_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='current_monthly_protection_payment',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Current Monthly Protection Payment'),
        ),
        migrations.AddField(
            model_name='expense',
            name='current_protection_coverage',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Current Protection Coverage'),
        ),
    ]
