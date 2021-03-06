# -*- coding:utf-8 -*-
import unittest
from sys import path
path.append('blackjack')
import blackjack.blackjack


class Testblackjack(unittest.TestCase):
    def setUp(self):
        self.obj = blackjack.blackjack.Blackjack()
        self.obj.creat_deck()
        self.money = 2000.00
        self.obj.bet(100, 10)
        self.obj.play()
        self.fake_hand = ['A♠', '10♣']

    def test_creat_deck(self):
        '''
        Function test the creation of decks. Increases the difficulty for the
        player. Maximum of 8 decks.
        '''
        # Test exception
        self.assertRaises(Exception, blackjack.blackjack.Blackjack.creat_deck, 10)
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
        self.assertEqual(self.obj.money, 1000.00)
        # For a bet invalid.
        self.assertRaises(Exception, blackjack.blackjack.Blackjack.bet, (3, 10))
        self.assertRaises(Exception, blackjack.blackjack.Blackjack.bet, (100, 30))

    def test_play(self):
        '''Function test of play.'''
        # For a deck normal.
        deck_size = len(self.obj.decks)
        self.assertEqual(deck_size, 48)
        # For a deck of eight decks.
        obj2 = blackjack.blackjack.Blackjack()
        obj2.creat_deck(8)
        obj2.bet(100, 10)
        obj2.play()
        deck_size = len(obj2.decks)
        self.assertEqual(deck_size, 412)
        # Test exception.
        self.assertRaises(Exception, blackjack.blackjack.Blackjack.play)

    def test_show_points(self):
        '''
        Function test of show points.
        '''
        fake_hand = ['A♠', '9♣']
        self.obj.show_points(fake_hand)
        self.assertEqual(self.obj.points, 10)
        # Test with a hand containing more of two cards.
        fake_hand3 = ['J♣', 'A♠', '8♣']
        self.obj.show_points(fake_hand3)
        self.assertEqual(self.obj.points, 19)

    def test_hit(self):
        '''
        Function test of hit.
        '''
        self.obj.show_points(self.fake_hand)
        self.obj.hit()
        self.assertEqual(len(self.obj.decks), 47)
        # Exception.
        fake_hand = ['J♣', 'A♠', '8♣']
        self.obj.show_points(fake_hand)
        self.assertRaises(Exception, blackjack.blackjack.Blackjack.hit)

    def test_hit_house(self):
        '''
        Function test of hit house.
        '''
        self.obj.show_points(self.fake_hand)
        self.obj.hit_house()
        self.assertEqual(len(self.obj.decks), 47)
        # Exception.
        fake_hand = ['J♣', 'A♠', '8♣']
        self.obj.show_points(fake_hand)
        self.assertRaises(Exception, blackjack.blackjack.Blackjack.hit_house)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
