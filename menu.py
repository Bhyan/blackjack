import os
import blackjack.blackjack


os.system('cls' if os.name == 'nt' else 'clear')
player = blackjack.blackjack.Blackjack()

decks = int(input(
    '''
    +-----------------------------------------------------------+
    |                                                           |
                        ♦ ♣ BLACKJACK ♠ ♥

        - Choose the number of decks (between one and eight).
    |                                                           |
    +-----------------------------------------------------------+
    Deck: '''))

player.creat_deck(decks)
os.system('cls' if os.name == 'nt' else 'clear')

coin = int(input(
    '''
    +-----------------------------------------------------------+
    |                                                           |
                        ♦ ♣ BLACKJACK ♠ ♥

                - You have 2000.00 coins for bet.
                   Coins: 1, 5, 10, 25, 50, 100.

            - You can bet more than one unit, only inform
                       the amount of chips.

                      - Exemple: Coin: 100
                             Quantity: 3
    |                                                           |
    +-----------------------------------------------------------+
    Coin: '''))
quantity = int(input('Quantity: '))

player.bet(coin, quantity)
os.system('cls' if os.name == 'nt' else 'clear')

player.play()
point_house = player.show_points(player.house)

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    point_player = player.show_points(player.hand)

    print(
        '''
        +-----------------------------------------------------------+
        |                                                           |
                            ♦ ♣ BLACKJACK ♠ ♥

            House: {} X         Your cards: {}

            Your points: {}               Your money: {}


                                Hit: Y/N
        |                                                           |
        +-----------------------------------------------------------+
        '''.format(player.house[0], player.hand, point_player, player.money))
    hit = input('Hit: ')
    hit.casefold()

    if point_player == 21:
        print('You won!')
    else:
        if hit == 'y':
            player.hit()
        elif hit == 'n':
            if point_house < point_player <= 21:
                print('House: {}'.format(player.house))
                print('Points of house: {}'.format(point_house))
                print('You won!')
                break
            elif point_player < point_house <= 21:
                print('House: {}'.format(player.house))
                print('Points of house: {}'.format(point_house))
                print('You lost!')
                break
            else:
                print('House: {}'.format(player.house))
                print('Points of house: {}'.format(point_house))
                print('Tie.')
                break
