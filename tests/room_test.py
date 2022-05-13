import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1= Room(1, 2, 50.00, 5.00)
        self.room2 = Room(2, 4, 50.00, 5.00)
        self.room3 = Room(3, 6, 50.00, 5.00)

        self.song1 = Song("Let it go", "Idina Menzel")
        self.song2 = Song("Sandman", "Metallica")
        self.song3 = Song("Summer of 69", "Bryan Adams")
        self.song4 = Song("Harvest Moon", "Neil Young")

        self.guest1 = Guest("Mia", 10.00, self.song1)
        self.guest2 = Guest("Aaron", 30.00, self.song2)
        self.guest3 = Guest("Kay", 30.00, self.song3)
        self.guest4 = Guest("Sarah", 40.00, self.song4)

    def test_room_has_number(self):
        self.assertEqual(1, self.room1.number)

    def test_room_has_capacity(self):
        self.assertEqual(4, self.room2.capacity)

    def test_room_has_till(self):
        self.assertEqual(50.00, self.room2.till)

    def test_room_has_fee(self):
        self.assertEqual(5.00, self.room3.fee)

    def test_check_in_guests(self):
        self.room1.check_in_guest(self.guest1)
        self.assertEqual(1, self.room1.room_guest_count())

    def test_check_out_guest_from_room(self):
        self.room2.check_in_guest(self.guest2)
        self.room2.check_in_guest(self.guest3)
        self.room2.check_out_guest(self.guest2)
        self.assertEqual(1, self.room2.room_guest_count())

    def test_add_songs_to_room(self):
        self.room1.add_song_to_room(self.song1)
        self.assertEqual(1, self.room1.room_song_count())

    def test_remove_song_from_room(self):
        self.room2.add_song_to_room(self.song1)
        self.room2.add_song_to_room(self.song2)
        self.room2.add_song_to_room(self.song3)
        self.room2.remove_song_from_room(self.song3)
        self.assertEqual(2, self.room2.room_song_count())

    





    



