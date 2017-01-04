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
                    self.decks.append('{}{}'.format(number, suit))
        return shuffle(self.decks)

    def bet(self, coin, quantity=1):
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
            return self.money

    def play(self):
        '''
        To start the function it is necessary to have a bet, that is why the
        variable self.money receives 0.01 in the betting function, ensuring
        that a bet was made. Remember that function remove 4 cards of decks.
        '''
        self.hand = []
        self.house = []
        while len(self.hand) < 2:
            self.hand.append(self.decks.pop(0))
            self.house.append(self.decks.pop(0))
        return self.hand, self.house

    def show_points(self, cards):
        '''
        Function counting the value of the cards. According to the rule if you
        have an Ace and a J, complete the value 21 or Blackjack.
        '''
        self.points = 0
        for card in cards:
            value = card[:-1]
            if value == 'A':
                self.points += 1
            elif value in ('J', 'Q', 'K'):
                self.points += 10
            else:
                self.points += int(value)
        return self.points

    def hit(self):
        '''
        Purchase function of cards. Allows purchase while value of sum of cards
        is lower than 21.
        '''
        if self.points < 21:
            self.hand.append(self.decks.pop(0))
        else:
            raise Exception(None)
        return self.hand

    def hit_house(self):
        '''
        Purchase function of cards. Allows purchase while value of sum of cards
        is lower than 21.
        '''
        self.house.append(self.decks.pop(0))
        return self.house
