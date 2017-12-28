# -*- coding:utf-8 -*-
import blackjack.blackjack


player = blackjack.blackjack.Blackjack()
blackjack.blackjack.header()
print('''The number of decks goes from one to eight, the larger the amount the
        greater the difficulty''')
decks = int(input('Insert the quantify of decks: '))
while player.money > 0.0:
    player.creat_deck(decks)
    blackjack.blackjack.header()
    print('Your money is: {} coins'.format(player.money))
    print('''For bet possible coin = 1, 5, 10, 25, 50 and 100. Is possible
        multiply the coins, not exceed your coins.''')
    coin = int(input('Coin: '))
    quantity = int(input('Quantity: '))
    player.bet(coin, quantity)
    player.play()
    while True:
        player_points = player.show_points(player.hand)
        house_points = player.show_points(player.house)
        blackjack.blackjack.header()
        print('Your cards: {}'.format(player.hand))
        print('Your points: {}'.format(player_points))
        print('Cards of house: [{}, X]'.format(player.house[0]))
        if player_points < 21:
            hit = input('More one card? [Y/N]')
            hit.casefold()
            if hit == 'y':
                player.hit()
            elif hit == 'n':
                while player_points >= house_points < 21:
                    player.hit_house()
                    house_points = player.show_points(player.house)
                    if player_points < house_points <= 21:
                        blackjack.blackjack.header()
                        print('Your cards: {}'.format(player.hand))
                        print('Your points: {}'.format(player_points))
                        print('Cards of house: {}'.format(player.house))
                        print('Points of house: {}'.format(house_points))
                        print('You lost.')
                        break
                    elif player_points > house_points:
                        blackjack.blackjack.header()
                        print('Your cards: {}'.format(player.hand))
                        print('Your points: {}'.format(player_points))
                        print('Cards of house: {}'.format(player.house))
                        print('Points of house: {}'.format(house_points))
                        print('You won.')
                        player.money += (coin * quantity) * 2
                        break
                    elif player_points == house_points:
                        blackjack.blackjack.header()
                        print('Your cards: {}'.format(player.hand))
                        print('Your points: {}'.format(player_points))
                        print('Cards of house: {}'.format(player.house))
                        print('Points of house: {}'.format(house_points))
                        print('Tie.')
                        player.money += (coin * quantity)
                        break
                    elif house_points > 21:
                        blackjack.blackjack.header()
                        print('Your cards: {}'.format(player.hand))
                        print('Your points: {}'.format(player_points))
                        print('Cards of house: {}'.format(player.house))
                        print('Points of house: {}'.format(house_points))
                        print('You won.')
                        player.money += (coin * quantity) * 2
                        break
                    break
                break
        elif player_points == 21:
            print('You won.')
            player.money += (coin * quantity) * 2
            break
        else:
            print('You lost.')
            break
