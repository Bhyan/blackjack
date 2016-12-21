# -*- coding:utf-8 -*-
import unittest
import blackjack


class TestBlackjack(unittest.TestCase):
    def setUp(self):
        self.deck = blackjack.creat_deck()
        self.decks = blackjack.creat_deck(deck=8)
        suits = ["♣", "♦", "♥", "♠"]
        numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Q",
                        "J", "K"]
        self.money = 2000.00

    def test_creat_deck(self):
        '''
        Function test the creation of decks. Increases the difficulty for the
        player. Maximum of 8 decks.
        '''
        # Creation of a common deck.
        deck_size = len(self.deck)
        self.assertEqual(deck_size, 52)
        # Creation of a deck of eight decks.
        decks_size = len(self.decks)
        self.assertEqual(decks_size, 416)

    def test_shuffle(self):
        '''
        Function test the shuffle of deck.
        '''
        # Shuffle of a normal deck.
        deck_before = self.deck[0:51]
        blackjack.shuffle(self.deck)
        deck_after = self.deck[0:51]
        self.assertNotEqual(deck_before, deck_after)
        # Shuffle of a deck of eight decks.
        decks_before = self.decks[0:415]
        blackjack.shuffle(self.decks)
        decks_after = self.decks[0:415]
        self.assertNotEqual(decks_before, decks_after)

    def test_bet(self):
        '''Function test of bet.'''
        # For a bet valid.
        coin = 100
        quantity = 10
        self.money -= (coin * quantity)
        self.assertEqual(self.money, 1000.00)
        # For a bet invalid.
        self.assertRaises(Exception, blackjack.bet(1, 10))

    def test_play(self):
        '''Function test of play.'''
        # For a deck normal.
        blackjack.shuffle(self.deck)
        self.deck.pop(0)
        self.assertEqual(len(self.deck), 51)
        # For a deck of eight decks.
        blackjack.shuffle(self.decks)
        self.decks.pop(0)
        self.assertEqual(len(self.decks), 415)
        # For exception.
        self.assertRaises(Exception, blackjack.play())

    def test_show_hand(self):
        '''
        Function test of show hand, where is create a new fake hand for test.
        '''
        fake_hand = ['A♣','10♣']
        cards = ', '.join(fake_hand)
        self.assertTrue(cards, 'A♣, 10♣')


    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
