class Room:

    def __init__(self, number, capacity, till, fee):
        self.number = number
        self.capacity = capacity
        self.till = till
        self.fee = fee
        self.songs = []
        self.guests = []

    def room_guest_count(self):
        return len(self.guests)

    def check_in_guest(self, guest):
        self.guests.append(guest)

    def check_out_guest(self, guest):
        self.guests.remove(guest)

    def room_song_count(self):
        return len(self.songs)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def remove_song_from_room(self, song):
        self.songs.remove(song)
