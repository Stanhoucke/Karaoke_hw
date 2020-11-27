class Guest():

    def __init__(self, input_name, input_age, input_wallet):
        self.name = input_name
        self.age = input_age
        self.wallet = input_wallet

    def pay_entry_fee(self):
        entry_fee = 9.95
        if self.wallet >= entry_fee:
            self.wallet -= 9.95
            return True
        else:
            return False