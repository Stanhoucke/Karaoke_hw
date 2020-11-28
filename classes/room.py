class Room():

    def __init__(self, input_room_number, input_capacity):
        self.room_number = input_room_number
        self.playlist = []
        self.guests = []
        self.capacity = input_capacity
        self.tab = 0.00

    def add_song(self, song):
        self.playlist.append(song)

    def remove_guest(self, guest_to_remove):
        self.guests.remove(guest_to_remove)

    def check_capacity(self, room_to_check):
        if len(room_to_check.guests) < room_to_check.capacity:
            return True
        else:
            return False

    def clear_room(self, room_to_clear):
        room_to_clear.guests.clear()
        room_to_clear.playlist.clear()
        room_to_clear.tab = 0.00

    def add_drink_to_tab(self, buying_guest, drink_to_buy):
        if buying_guest.pay_for_drink(drink_to_buy):
            self.tab += drink_to_buy.price

    def add_entry_fee_to_tab(self, guest):
        entry_fee = 9.95
        if guest.pay_entry_fee():
            self.tab += entry_fee
            return True
        else:
            return False

    def favourite_song_on_playlist(self):
        pass

    def play_song(self):
        pass

    def add_guest(self, guest_to_add, room_to_check):
        # Check room has capacity
        if room_to_check.check_capacity(room_to_check):
            # Check guest can afford entry
            if self.add_entry_fee_to_tab(guest_to_add):
                # Add guest
                self.guests.append(guest_to_add)
    