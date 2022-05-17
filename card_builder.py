import random
# This function and file create the deck,


# This function will take a queue as an arguemnt, make sure that it is blank, and then build a deck
# made of 4 full decks of cards
def build_deck(deck):
    deck.clear()
    values = ['Ace', '2', '3', '4', '5', '6', '7',
              '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
    for i in range(4):
        for value in values:
            for suit in suits:
                deck.append((f'{value} of {suit}'))
    random.shuffle(deck)


# This function returns the int value of the cards.
# The 'split' works to grab the first number if it is not a
# face card or an Ace. I.E '10 of Clubs' will return 10
def card_number_values(card):
    if "Ace" in card:
        return 11
    elif "King" in card or "Queen" in card or "Jack" in card:
        return 10
    else:
        num = int(card.split(" ")[0])
        return num
