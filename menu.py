import os
import blackjack.blackjack


os.system('cls' if os.name == 'nt' else 'clear')
player = blackjack.blackjack.Blackjack()
house = blackjack.blackjack.Blackjack()

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

    if point_player == 21:
        print('You won!')
        break
    elif point_player > 21:
        print('You lost!')
        break

    hit = input('Hit: ')
    hit.casefold()

    if hit == 'y':
        player.hit()
    elif hit == 'n':
        break
