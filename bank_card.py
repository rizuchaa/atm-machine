#   inisiasi set awal kartu
class bank_card:
    # finish
    def __init__(self, pin, balance):
        self.set_pin = pin
        self.set_balance = balance

    def check_set_pin(self):
        return self.set_pin

    def check_set_bal(self):
        return self.set_balance
