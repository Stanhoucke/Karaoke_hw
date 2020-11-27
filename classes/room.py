class Room():

    def __init__(self, input_room_number):
        self.room_number = input_room_number
        self.playlist = []
        self.guests = []

    def add_song(self, song):
        self.playlist.append(song)