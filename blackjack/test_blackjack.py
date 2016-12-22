# -*- coding:utf-8 -*-
import unittest
import blackjack


class TestBlackjack(unittest.TestCase):
    def setUp(self):
        self.obj = blackjack.Blackjack()
        self.obj.creat_deck()
        self.money = 2000.00
        self.obj.bet(100, 10)
        self.obj.play()

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
        self.assertEqual(self.obj.money, 1000.01)
        # For a bet invalid.
        self.assertRaises(Exception, blackjack.Blackjack.bet, (3, 10))
        self.assertRaises(Exception, blackjack.Blackjack.bet, (100, 30))

    def test_play(self):
        '''Function test of play.'''
        # For a deck normal.
        deck_size = len(self.obj.decks)
        self.assertEqual(deck_size, 48)
        # For a deck of eight decks.
        obj2 = blackjack.Blackjack()
        obj2.creat_deck(8)
        obj2.bet(100, 10)
        obj2.play()
        deck_size = len(obj2.decks)
        self.assertEqual(deck_size, 412)
        # Test exception
        self.assertRaises(Exception, blackjack.Blackjack.play)

    def test_show_hand(self):
        '''
        Function test of show hand.
        '''
        self.obj.show_hand()
        size_hand = len(self.obj.hand)
        self.assertTrue(size_hand, 2)

    def test_show_points(self):
        '''
        Function test of show points.
        '''
        fake_hand = ['A♠', '10♣']
        self.obj.show_points(fake_hand)
        self.assertEqual(self.obj.points, 11)
        fake_hand = ['A♠', '9♣']
        self.obj.show_points(fake_hand)
        self.assertEqual(self.obj.points, 10)
        # Fake blackjack
        fake_blackjack = ['A♠', 'J♣']
        self.obj.show_points(fake_blackjack)
        self.assertEqual(self.obj.points, 21)
        fake_blackjack2 = ['J♣', 'A♠']
        self.obj.show_points(fake_blackjack2)
        self.assertEqual(self.obj.points, 21)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
