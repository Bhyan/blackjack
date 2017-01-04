# -*- coding:utf-8 -*-
import blackjack.blackjack
import os


os.system('cls' if os.name == 'nt' else 'clear')
player = blackjack.blackjack.Blackjack()
print('+', '-' * 60, '♦ ♣ BLACKJACK ♠ ♥', '-' * 60, '+\n')
print('''The number of decks goes from one to eight, the larger the amount the
        greater the difficulty''')
decks = int(input('Insert the quantify of decks: '))
player.creat_deck(decks)
# print(len(player.decks))
while player.money > 0.0:
    print('+', '-' * 60, '♦ ♣ BLACKJACK ♠ ♥', '-' * 60, '+\n')
    print('Your money is: {} coins'.format(player.money))
    print('''For bet possible coin = 1, 5, 10, 25, 50 and 100. Is possible
        multiply the coins, not exceed your coins.''')
    coin = int(input('Coin: '))
    quantity = int(input('Quantity: '))
    player.bet(coin, quantity)
    player.play()
    while True:
        player.show_points(player.hand)
        print('+', '-' * 60, '♦ ♣ BLACKJACK ♠ ♥', '-' * 60, '+\n')
        print('Your cards: {}'.format(player.hand))
        print('Your points: {}'.format(player.points))
        print('Cards of house: [{}, X]'.format(player.house[0]))
        if player.points < 21:
            hit = input('More one card? [Y/N]')
            hit.casefold()
            if hit == 'y':
                player.hit()
            elif hit == 'n':
                print('+', '-' * 60, '♦ ♣ BLACKJACK ♠ ♥', '-' * 60, '+\n')
                print('Your cards: {}'.format(player.hand))
                print('Your points: {}'.format(player.points))
                print('Cards of house: {}'.format(player.house))
                player.show_points(player.house)
                print('Points of house: {}'.format(player.points))
                break
        elif player.points == 21:
            print('You won.')
            break
        else:
            print('You lost.')
            break
