import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("Dignity", "Deacon Blue")
        
        self.guest1 = Guest("Nicole", 50.00, self.song1)
        

    def test_guest_has_name(self):
        self.assertEqual("Nicole", self.guest1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50.00, self.guest1.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual(self.song1, self.guest1.song)

        
        