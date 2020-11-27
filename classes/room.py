class Room():

    def __init__(self, input_room_number):
        self.room_number = input_room_number
        self.playlist = []
        self.guests = []

    def add_song(self, song):
        self.playlist.append(song)

    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self, guest):
        pass