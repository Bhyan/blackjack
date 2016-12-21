# -*- coding:utf-8 -*-
import unittest
import blackjack


class TestBlackjack(unittest.TestCase):
    def setUp(self):
        self.obj = blackjack.Blackjack()
        self.obj.creat_deck()
        self.money = 2000.00
        self.fake_hand = ['2♣', '10♣']

    def test_creat_deck(self):
        '''
        Function test the creation of decks. Increases the difficulty for the
        player. Maximum of 8 decks.
        '''
        # Creation of a common deck.
        self.obj.creat_deck()
        deck_size = len(self.obj.decks)
        self.assertEqual(deck_size, 52)
        # Creation of a deck of eight decks.
        self.obj.creat_deck(8)
        decks_size = len(self.obj.decks)
        self.assertEqual(decks_size, 416)

    def test_bet(self):
        '''Function test of bet.'''
        # For a bet valid.
        self.obj.bet(100, 10)
        self.assertEqual(self.obj.money, 1000.01)
        # For a bet invalid.
        self.assertRaises(Exception, blackjack.Blackjack.bet, (3, 10))
        self.assertRaises(Exception, blackjack.Blackjack.bet, (100, 30))

    def test_play(self):
        '''Function test of play.'''
        # For a deck normal.
        self.obj.bet(10, 10)
        self.obj.play()
        deck_size = len(self.obj.decks)
        self.assertEqual(deck_size, 48)
        # For a deck of eight decks.
        self.obj.play()
        deck_size = len(self.obj.decks)
        self.assertEqual(deck_size, 44)
        # Test exception
        self.assertRaises(Exception, blackjack.Blackjack.play)

    def test_show_hand(self):
        '''
        Function test of show hand, where is create a new fake hand for test.
        '''
        cards = ', '.join(self.fake_hand)
        self.assertTrue(cards, '2♣, 10♣')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
