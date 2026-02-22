import unittest
from TDD.aplikacja import Czlowiek

class TestCzlowiek(unittest.TestCase):
    def setUp(self):
        self.czlowiek = Czlowiek("Stasio")
    # Metody testowe
    # Zaczynają się od słowa test...
    def test_przedstaw_sie(self):
        przedstawienie_str = self.czlowiek.przedstaw_sie()
        self.assertEqual("Cześć, jestem Stasio", przedstawienie_str)
    def tearDown(self):
        del self.czlowiek
if __name__ == "__main__":
    unittest.main(verbosity=2)