import random
import time
from card_builder import build_deck
from card_builder import card_number_values

values = ['Ace', '2', '3', '4', '5', '6', '7',
          '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
play_deck = []
amount_of_tokens = 1000
yes_response = ["1", "yes", "y"]
no_response = ["2", "no", "n"]


def initial_deal():
    card_1_name = play_deck.pop(random.randrange(len(play_deck)))
    card_1_value = card_number_values(card_1_name)
    card_2_name = play_deck.pop(random.randrange(len(play_deck)))
    card_2_value = card_number_values(card_2_name)
    card_list = [card_1_name, card_1_value, card_2_name, card_2_value]

    return card_list


def hit(cards):
    card_name = play_deck.pop(random.randrange(len(play_deck)))
    card_value = card_number_values(card_name)
    cards.append(card_name)
    cards.append(card_value)

    return cards


def play_game(p_total, p_cards, d_total, d_cards, bet):
    global amount_of_tokens
    bust = False
    aces = 0
    if "Ace" in p_cards[0] or "Ace" in p_cards[2]:
        aces = 1
    hit_or_stay = str(
        input("1.) Hit\n2.) Stay\nWhat would you like to do: ").lower())
    while hit_or_stay in ["1", "hit"]:
        hit(p_cards)
        p_total += int(p_cards[-1])
        print("You get the {} for a new total of {}".format(
            p_cards[-2], p_total))
        if "Ace" in p_cards[-2] or aces > 0:
            aces += 1
            p_total -= 10
            p_cards[-1] -= 10
            print("However, your {} will be changed from 11 to 1, to prevent you from busting. Your new total is {}".format(
                p_cards[-2], p_total))
            aces -= 1
            break
        elif p_total > 21:
            print("You bust and lose your bet!")
            bust = True
            break
        else:
            hit_or_stay = str(
                input("1.) Hit\n2.) Stay\nWhat would you like to do: ").lower())
    if bust == True:
        return

    print(
        f"You have chosen to stay at {p_total}. The dealer flips over their face down card to reveal the {d_cards[2]}, for a new total of {d_total}")
    while d_total <= 16:
        hit(d_cards)
        d_total += d_cards[-1]
        print("The dealer has less than 17, and must hit. The dealer gets a {} for a new total of {}".format(
            d_cards[-2], d_total))
    print("The dealer has 17 or more, and must stay.")
    if d_total > 21:
        winnings = bet*2
        amount_of_tokens += winnings
        print(
            f"The dealer busts! You get back {winnings} tokens for a new total of {amount_of_tokens}!")
    elif d_total > p_total:
        print("The dealer has beaten you! You lose your bet!")
    elif d_total == p_total:
        amount_of_tokens += bet
        print("Push! You get your bet back!")
    else:
        winnings = bet*2
        amount_of_tokens += winnings
        print(
            f"You have beaten the dealer! You get back {winnings} tokens for a new total of {amount_of_tokens}!")


def clear(p_total, p_cards, d_total, d_cards):
    p_cards.clear()
    d_cards.clear()
    p_total = 0
    d_total = 0


play_game_flag = True

print(""" 
 ___   _      __    __    _       _    __    __    _    
| |_) | |    / /\  / /`  | |_/   | |  / /\  / /`  | |_/ 
|_|_) |_|__ /_/--\ \_\_, |_| \ \_|_| /_/--\ \_\_, |_| \         
    \n\n          === Welcome to Wild Bills Blackjack Hall! ===          """)

while play_game_flag:
    play_choice = str(input(
        "1.) Yes\n2.) No\nWould you like to play some BlackJack: ").lower())
    if play_choice in yes_response:
        print("You have been given 1000 tokens to play!\nThis game is played with 4 decks of cards, so you may see some repeats!")
        break
    elif play_choice in no_response:
        play_game_flag = False
        print("Come back real soon!")
        break
    else:
        print("That wasn't an option pardner!\n")

while play_game_flag:

    if len(play_deck) < 15:
        print("Shuffling deck. . .")
        time.sleep(1)
        build_deck(play_deck)

    bet = int(input(
        f"You have {amount_of_tokens} tokens.\nHow much would you like to bet on this hand: "))
    amount_of_tokens -= bet
    print("\nYour new total is {} tokens.\n".format(amount_of_tokens))
    player_cards_list = initial_deal()
    dealer_cards_list = initial_deal()
    player_total = player_cards_list[1] + player_cards_list[3]
    dealer_total = dealer_cards_list[1] + dealer_cards_list[3]

    print("You get the {} and the {}, for a total value of: {}\nThe dealer is showing the {} for a total of: {}".format(
        player_cards_list[0], player_cards_list[2], player_total, dealer_cards_list[0], dealer_cards_list[1]))

    if player_total == 21:
        winnings = bet*2.5
        amount_of_tokens += winnings
        print("=== Winner Winner Chicken Dinner ===")
        print("You have won {}, bringing your new total to: {} tokens!".format(
            winnings, amount_of_tokens))
    elif player_total == 22:
        player_total -= 10
        print("You started with two aces, so your total will start at {}".format(
            player_total))
        play_game(player_total, player_cards_list,
                  dealer_total, dealer_cards_list, bet)
    elif dealer_total == 21:
        print("The dealer flips over their 2nd card to revealing a {}. A natural 21! Unlucky! Your new total is {} tokens".format(
            dealer_cards_list[3], amount_of_tokens))
    else:
        play_game(player_total, player_cards_list,
                  dealer_total, dealer_cards_list, bet)

    play_again = input("1.) Yes\n2.) No\nWould you like to keep playing: ")
    if play_again in yes_response:
        clear(player_total, player_cards_list,
              dealer_total, dealer_cards_list)
    else:
        print("Come back soon!")
        play_game_flag = False
