import uuid

from computedfields.models import computed, ComputedFieldsModel
from django.db import models
from datetime import date
from .client import Client
from .partner import Partner

# We would leave the factor fields alone since they're basically configurable constants We need to change the value
# and range fields to @computed based on client.birth_year and client.annual_net_income + client.additional_income

class Plan(ComputedFieldsModel):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    client = models.OneToOneField(
        to=Client,
        on_delete=models.CASCADE)
    partner = models.OneToOneField(
        to=Partner,
        on_delete=models.CASCADE)
    protection_factor_upper = models.DecimalField(
        "Protection Factor Upper",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    protection_factor_lower = models.DecimalField(
        "Protection Factor Lower",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    protection_range_upper = models.DecimalField(
        "Protection Range Upper",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    protection_range_lower = models.DecimalField(
        "Protection Range Lower",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    emergency_savings_factor_upper = models.DecimalField(
        "Emergency Savings Factor Upper",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    emergency_savings_factor_lower = models.DecimalField(
        "Emergency Savings Factor Lower",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    emergency_savings_range_upper = models.DecimalField(
        "Emergency Savings Range Upper",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    emergency_savings_range_lower = models.DecimalField(
        "Emergency Savings Range Lower",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    budget_savings_factor = models.DecimalField(
        "Budget Savings Factor",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    budget_savings_value = models.DecimalField(
        "Budget Savings Value",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    budget_fixed_expenses_factor = models.DecimalField(
        "Budget Fixed Expenses Factor",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    budget_fixed_expenses_value = models.DecimalField(
        "Budget Fixed Expenses Value",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    budget_spending_factor = models.DecimalField(
        "Budget Spending Factor",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    budget_spending_value = models.DecimalField(
        "Budget Spending Value",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    debt_repayment_factor = models.DecimalField(
        "Debt Repayment Factor",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    debt_repayment_value = models.DecimalField(
        "Debt Repayment Value",
        max_digits=8,
        decimal_places=2,
        default=0.0)
    household_annual_net_income = models.DecimalField(
        "Household Annual Net Income",
        max_digits=8,
        decimal_places=2,
        default=0.0)

    @computed(models.FloatField("Retirement Factor", default=1.0), depends=['client#age'])
    def retirement_factor(self):
        client_age = self.client.age
        if client_age < 39:
            self.retirement_factor = 1.0
        elif 40 <= client_age <= 49:
            self.retirement_factor = 3.0
        elif 50 <= client_age <= 59:
            self.retirement_factor = 6.0
        elif 60 <= client_age <= 66:
            self.retirement_factor = 8.0
        elif client_age >= 67:
            self.retirement_factor = 10.0
        else:
            self.retirement_factor = 1.0
        return self.retirement_factor

    @computed(models.FloatField("Recommended Retirement Value", default=0.0),
              depends=['client#total_annual_income'])
    def recommended_retirement_value(self):
        return self.retirement_factor * self.client.total_annual_income

    @computed(models.IntegerField(default=0), depends=['client#personal_annual_net_income', 'partner#personal_annual_net_income'])
    def household_annual_income(self):
        household_annual_income_ouput = self.client.personal_annual_net_income + self.client.additional_income + self.partner.personal_annual_net_income
        return household_annual_income_ouput

    def __str__(self):
        attrs = vars(self)
        return '\n'.join('%s: %s' % item for item in attrs.items())
