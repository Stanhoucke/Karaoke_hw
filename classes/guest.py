class Guest():

    def __init__(self, input_name, input_age, input_wallet, input_favourite_song):
        self.name = input_name
        self.age = input_age
        self.wallet = input_wallet
        self.favourite_song = input_favourite_song

    def pay_entry_fee(self):
        entry_fee = 9.95
        if self.wallet >= entry_fee:
            self.wallet -= 9.95
            return True
        else:
            return False

    def pay_for_drink(self, drink_to_buy):
        if self.age < 18 and drink_to_buy.alcoholic:
            return False
        elif self.wallet < drink_to_buy.price:
            return False
        else:
            self.wallet -= drink_to_buy.price
            return True