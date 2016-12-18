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

DECK = creat_deck()
# Shuffle of deck.
shuffle(DECK)
# pdb.set_trace()
