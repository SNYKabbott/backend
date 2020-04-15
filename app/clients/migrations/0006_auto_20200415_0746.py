# Generated by Django 2.2.10 on 2020-04-15 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_debt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='bills_housing',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='bills_insurance',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='bills_loan_or_debt',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='bills_other',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='bills_utilities',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='expense_leisure',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='expense_shopping',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='expense_subscriptions',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='expense_transportation',
        ),
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Amount'),
        ),
        migrations.AddField(
            model_name='expense',
            name='category',
            field=models.CharField(choices=[('House_Mortgage', 'House Mortgage'), ('House_Rent', 'House Rent'), ('Utilities', 'Utilities'), ('Insurance', 'Insurance'), ('Shopping', 'Shopping'), ('Leisure', 'Leisure'), ('Transportation', 'Transportation'), ('Subscription', 'Subscription'), ('Other', 'Other')], default='Other', max_length=20),
        ),
        migrations.AlterField(
            model_name='debt',
            name='debt_interest_rate',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Debt Interest Rate'),
        ),
        migrations.AlterField(
            model_name='expense',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
        ),
    ]
