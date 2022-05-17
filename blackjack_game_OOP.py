from card_builder import build_deck
from card_builder import card_number_values
import random

# Global Variables
play_deck = []
build_deck(play_deck)
yes_response = ["1", "yes", "y"]
no_response = ["2", "no", "n"]
play_game_flag = True


class Dealer:
    def __init__(self):
        self.card_name = []
        self.card_value = []
        self.total = 0

    def reset_hand(self):
        self.card_name.clear()
        self.card_value.clear()
        self.total = 0

    def initial_deal(self):
        self.card_name.append(play_deck.pop(random.randrange(len(play_deck))))
        self.card_value.append(card_number_values(self.card_name[0]))
        self.card_name.append(play_deck.pop(random.randrange(len(play_deck))))
        self.card_value.append(card_number_values(self.card_name[1]))
        self.total = sum(self.card_value)

    def hit(self):
        self.card_name.append(play_deck.pop(random.randrange(len(play_deck))))
        self.card_value.append(card_number_values(self.card_name[-1]))
        self.total = sum(self.card_value)

    def play_game(self, player):
        bust = False
        aces = 0
        if "Ace" in player.card_name[1]:
            aces = 1
        hit_or_stay = str(
            input("1.) Hit\n2.) Stay\nWhat would you like to do: ").lower())
        while hit_or_stay in ["1", "hit"]:
            player.hit()
            print("You get the {} for a new total of {}".format(
                player.card_name[-1], player.total))
            if "Ace" in player.card_name[-1]:
                player.total -= 10
                player.card_value[-1] -= 10
                print("However, your {} will be changed from 11 to 1, to prevent you from busting. Your new total is {}".format(
                    player.card_name[-1], player.total))
                break
            elif aces > 0:
                player.total -= 10
                player.card_value[1] -= 10
                print("However, your {} will be changed from 11 to 1, to prevent you from busting. Your new total is {}".format(
                    player.card_name[1], player.total))
            elif player.total > 21:
                print("You bust and lose your bet!")
                bust = True
                break
            else:
                hit_or_stay = str(
                    input("1.) Hit\n2.) Stay\nWhat would you like to do: ").lower())
        if bust == True:
            return

        print(
            f"You have chosen to stay at {player.total}. The dealer flips over their face down card to reveal the {dealer.card_name[1]}, for a new total of {dealer.total}")
        while dealer.total <= 16:
            dealer.hit()
            print("The dealer has less than 17, and must hit. The dealer gets a {} for a new total of {}".format(
                dealer.card_name[-1], dealer.total))
        print("The dealer has 17 or more, and must stay.")
        if dealer.total > 21:
            winnings = bet*2
            player.tokens += winnings
            print(
                f"The dealer busts! You get back {winnings} tokens for a new total of {player.tokens}!")
        elif dealer.total > player.total:
            print("The dealer has beaten you! You lose your bet!")
        elif dealer.total == player.total:
            player.tokens += bet
            print("Push! You get your bet back!")
        else:
            winnings = bet*2
            player.tokens += winnings
            print(
                f"You have beaten the dealer! You get back {winnings} tokens for a new total of {player.tokens}!")


class Player(Dealer):
    def __init__(self):
        super().__init__()
        self.tokens = 1000


class Game:

    @classmethod
    def game_start(self):
        global play_game_flag
        play_choice = str(input(
            "1.) Yes\n2.) No\nWould you like to play some BlackJack: ").lower())
        if play_choice in yes_response:
            print("You have been given 1000 tokens to play!\nThis game is played with 4 decks of cards, so you may see some repeats!")

        elif play_choice in no_response:
            print("Come back real soon!")
            play_game_flag = False

        else:
            print("That wasn't an option pardner!\n")


dealer = Dealer()
player = Player()

print("""
 ___   _      __    __    _       _    __    __    _
| |_) | |    / /\  / /`  | |_/   | |  / /\  / /`  | |_/
|_|_) |_|__ /_/--\ \_\_, |_| \ \_|_| /_/--\ \_\_, |_| \
    \n\n          === Welcome to Wild Bills Blackjack Hall! ===          """)
Game.game_start()

while play_game_flag:
    if len(play_deck) < 15:
        print("Shuffling deck. . .")
        build_deck(play_deck)

    bet = int(input(
        f"You have {player.tokens} tokens.\nHow much would you like to bet on this hand: "))
    player.tokens -= bet
    print("\nYour new total is {} tokens.\n".format(player.tokens))

    dealer.initial_deal()
    player.initial_deal()

    print("You get the {} and the {}, for a total value of: {}\nThe dealer is showing the {} for a total of: {}\n".format(
        player.card_name[0], player.card_name[1], player.total, dealer.card_name[0], dealer.card_value[0]))

    if player.total == 21:
        winnings = bet*2.5
        player.tokens += winnings
        print("=== Winner Winner Chicken Dinner ===")
        print("You have won {}, bringing your new total to: {} tokens!".format(
            winnings, player.tokens))
    elif player.total == 22:
        player.card_value[0] -= 10
        player.total -= 10
        print("You started with two aces, so your total will start at {}".format(
            player.total))
    elif dealer.total == 21:
        print("The dealer flips over their 2nd card to revealing a {}. A natural 21! Unlucky! Your new total is {} tokens".format(
            dealer.card_name[1], player.tokens))
    else:
        dealer.play_game(player)

    play_again = input("1.) Yes\n2.) No\nWould you like to keep playing: ")
    if play_again in yes_response:
        dealer.reset_hand()
        player.reset_hand()
    else:
        print("Come back soon!")
        play_game_flag = False
