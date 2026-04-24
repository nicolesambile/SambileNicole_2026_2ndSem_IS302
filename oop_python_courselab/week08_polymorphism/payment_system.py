class Payment_nbs:
    def pay_nbs(self_nbs):
        print("Processing payment")

class CashPayment_nbs(Payment_nbs):
    def pay_nbs(self_nbs):
        print("Payment made using cash")

class CardPayment_nbs(Payment_nbs):
    def pay_nbs(self_nbs):
        print("Payment made using credit card")

payments_nbs = [CashPayment_nbs(), CardPayment_nbs()]
for p_nbs in payments_nbs:
    p_nbs.pay_nbs()

#Nicole Sambile