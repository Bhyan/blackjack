#!/usr/bin/env python
# -*- coding:utf-8 -*-
from random import shuffle
import pdb


def creat_deck(deck=1):
    '''
    Create card function, it is possible to create a deck with more cards.
    Increases the difficulty for the player. Maximum of 8 decks.
    '''
    suits = ["♣", "♦", "♥", "♠"]
    numbers = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Q",
                    "J", "K"]
    decks = []
    count = 0

    while count < deck:
        count += 1
        for suit in suits:
            for number in numbers:
                decks.append('{}{}'.format(suit, number))
    return decks

    def bet(coin, quantity):
        '''
        Betting values are defined as casino chips. That is why exist the
        exception error.
        '''
        global MONEY
        if coin not in (1, 5, 10, 25, 50, 100):
            raise Exception('Invalid coin for bet.')
        elif MONEY < (coin * quantity):
            raise Exception('Value of bet larger what your money.')
        else:
            MONEY -= (coin * quantity)
        return MONEY += 0.01

    def play():
        '''
        To start the function it is necessary to have a bet, that is why the
        variable MONEY receives 0.01 in the betting function, ensuring that a
        bet was made.
        '''
        if MONEY == 2000.00:
            raise Exception('Bet is necessary for player.')
        else:
            while len(HAND) < 2:
                HAND.append(DECK.pop(0))
                HOUSE.append(DECK.pop(0))
            return HAND, HOUSE

DECK = creat_deck()
# Shuffle of deck.
shuffle(DECK)
# pdb.set_trace()
MONEY = 2000.00
HAND = []
HOUSE = []
