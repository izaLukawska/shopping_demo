from shopping.payment import CardPayment, PaymentProcessor, CashPayment


def test_process_card_payment():
    # given
    card_payment = CardPayment()
    payment_processor = PaymentProcessor(card_payment)

    # when
    result = payment_processor.process(20.22)

    # then
    assert result == 'Card payment of $20.22 successful'

def test_process_cash_payment():
    # given
    cash_payment = CashPayment()
    payment_processor = PaymentProcessor(cash_payment)

    # when
    result = payment_processor.process(20.22)

    # then
    assert result == 'Cash payment of $20.22 successful'
