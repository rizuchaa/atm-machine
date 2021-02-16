# import bank_card as bc


class customer:
    def __init__(self, id, pin=1234, balance=10000):
        self.cust_id = id
        self.cust_pin = pin
        self.cust_bal = balance

    def check_id_card(self):
        return self.cust_id

    def check_pin(self):
        return self.cust_pin

    def check_bal(self):
        return self.cust_bal

    def get_debit(self, nominal):
        self.cust_bal -= nominal

    def last_balance(self, nominal):
        self.cust_bal += nominal
