class Room():

    def __init__(self, input_room_number, input_capacity):
        self.room_number = input_room_number
        self.playlist = []
        self.guests = []
        self.capacity = input_capacity

    def add_song(self, song):
        self.playlist.append(song)

    def add_guest(self, guest_to_add):
        self.guests.append(guest_to_add)

    def remove_guest(self, guest_to_remove):
        self.guests.remove(guest_to_remove)

    def check_capacity(self, room_to_check):
        if len(room_to_check.guests) < room_to_check.capacity:
            return True