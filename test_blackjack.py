# -*- coding:utf-8 -*-
import unittest
import blackjack


class TestBlackjack(unittest.TestCase):
    def setUp(self):
        self.deck = blackjack.creat_deck()
        self.decks = blackjack.creat_deck(deck=2)
        suits = ["♣", "♦", "♥", "♠"]
        numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Q",
                        "J", "K"]

    def test_creat_deck(self):
        deck_size = len(self.deck)
        self.assertEqual(deck_size, 52)
        decks_size = len(self.decks)
        self.assertEqual(decks_size, 104)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
