from factory.fuzzy import FuzzyInteger, FuzzyText, FuzzyDecimal
from factory.django import DjangoModelFactory
from factory import SubFactory
from accounts.tests.factories import VokoUserFactory
from ordering.tests.factories import OrderFactory


class BalanceFactory(DjangoModelFactory):
    class Meta:
        model = "finance.Balance"

    user = SubFactory(VokoUserFactory)
    amount = FuzzyDecimal(low=1, high=99)


class PaymentFactory(DjangoModelFactory):
    class Meta:
        model = "finance.Payment"

    order = SubFactory(OrderFactory)
    amount = FuzzyDecimal(low=1, high=99)

    mollie_id = FuzzyText()

    qantani_transaction_id = FuzzyInteger(low=1, high=999)
    qantani_transaction_code = FuzzyText()
