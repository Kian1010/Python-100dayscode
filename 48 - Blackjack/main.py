from art import logo
import os
import random
#    Our Blackjack House Rules    #
# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def give_card(dealing_card: list):
    dealing_card.append(random.choice(cards))

    for i in range(len(dealing_card)):
        if dealing_card[i] == 11:
            if sum(dealing_card) > 21:
                dealing_card[i] = 1
    return dealing_card


def show_cards(p_card, d_card):
    print(f"Your cards: {p_card}, current score: {sum(p_card)}")
    print(f"Computer's first card: {d_card[0]}")


def blackjack():
    outcome = ""
    clear()
    print(logo)
    player_cards = []
    dealer_cards = []
    for x in range(2):
        give_card(player_cards)
        give_card(dealer_cards)
    show_cards(player_cards, dealer_cards)

    if sum(dealer_cards) == 21:
        outcome = "You Lose! Dealer has blackjack"
        continue_pickup = "N"
    elif sum(player_cards) == 21:
        outcome = "You win! You have blackjack"
        continue_pickup = "N"
    else:
        continue_pickup = input("Type 'y' to get another card, type 'n' to pass: ").upper()

    while continue_pickup == "Y":
        give_card(player_cards)
        show_cards(player_cards, dealer_cards)
        if sum(player_cards) > 21:
            continue_pickup = "N"
        else:
            continue_pickup = input("Type 'y' to get another card, type 'n' to pass: ").upper()

    while sum(dealer_cards) < 17:
        give_card(dealer_cards)

    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")

    if outcome == "":
        if sum(player_cards) > 21:
            print("You bust! You lose")
        elif sum(dealer_cards) > 21:
            print("Dealer busts! You win")
        elif sum(player_cards) == sum(dealer_cards):
            print("Draw!")
        elif sum(player_cards) > sum(dealer_cards):
            print("You win!")
        elif sum(dealer_cards) > sum(player_cards):
            print("You Lose!")
    else:
        print(outcome)
    start_game()


def start_game():
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").upper() == "Y":
        blackjack()


start_game()
