#!/usr/bin/env python
# -*- coding:utf-8 -*-
from random import shuffle


class Blackjack(object):
    def __init__(self):
        self.money = 2000.00

    def creat_deck(self, deck=1):
        '''
        Create card function, it is possible to create a deck with more cards.
        Increases the difficulty for the player. Maximum of 8 decks.
        '''
        suits = ["♣", "♦", "♥", "♠"]
        numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Q",
                        "J", "K"]
        self.decks = []
        count = 0
        while count < deck:
            count += 1
            for suit in suits:
                for number in numbers:
                    self.decks.append('{}{}'.format(suit, number))
        return shuffle(self.decks)

    def bet(self, coin, quantity):
        '''
        Betting values are defined as casino chips. That is why exist the
        exception error.
        '''
        if coin not in (1, 5, 10, 25, 50, 100):
            raise Exception('Invalid coin for bet.')
        elif self.money < (coin * quantity):
            raise Exception('Value of bet larger what your money.')
        else:
            self.money -= (coin * quantity)
            self.money += 0.01
            return self.money

    def play(self):
        '''
        To start the function it is necessary to have a bet, that is why the
        variable self.money receives 0.01 in the betting function, ensuring that a
        bet was made.
        '''
        self.hand = []
        self.house = []
        if self.money == 2000.00:
            raise Exception('Bet is necessary for player.')
        else:
            while len(self.hand) < 2:
                self.hand.append(self.decks.pop(0))
                self.house.append(self.decks.pop(0))
            return self.hand, self.house

    def show_hand(self):
        '''
        This function only shows the cards to the player. His and those in the
        house.
        '''
        msg = ('Your hand has {} card: {}')
        cards = ', '.join(self.hand)
        print(msg.format(len(self.hand), cards))
        print('House: {}, X'.format(self.house[0]))
