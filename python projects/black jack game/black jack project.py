import random
from art import logo
from clear_mod import cls
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
cards = [11, 10]
player_cards = []
dealers_cards = []
hit = ""
start_game = ''

def player_total (list = player_cards):
    sum = 0
    for total in list:
        sum += total
        if sum > 21 and total == 11:
            total = -10
            sum += total
    return(sum)

def dealer_total (list = dealers_cards):
    sum = 0
    for total in list:
        sum += total
        if sum > 21 and total == 11:
            total = -10
            sum += total
    return(sum)

def play_black_jack():
    start_game = input('Do you want to play Balck Jack. Type "y" to play or "n" for quit: ').lower() 
    while start_game == "y":
        cls()
        print(logo)
        player_cards = random.choices(cards, k=2)
        print(f"your cards are: {player_cards}, your total is {player_total(list = player_cards)}")
        dealers_cards = random.choices(cards, k=2)
        print(f"dealers card is: {dealers_cards[0]}, dealers total is {dealers_cards[0]}.")
        if player_total(list= player_cards) == 21 and len(player_cards) == 2:
            print("Player got Black Jack")
            hit = "n"
        else:
            hit = input('Type "y" to hit or "n" to stick: ').lower()
        while hit == "y":
            player_new_cards = random.choice(cards)
            player_cards.append(player_new_cards)
            print(f"your cards are {player_cards}, your total is {player_total(list = player_cards)}")

            if player_total(list= player_cards) > 21:
                print("Player Bust")
                hit = "n"
            else:
                hit = input('Type "y" to hit or "n" to stick: ').lower()
        
        while dealer_total(list = dealers_cards) < 17:
            dealer_new_cards = random.choice(cards)
            dealers_cards.append(dealer_new_cards)
        print(f"The dealers cards are {dealers_cards}, the dealers total is {dealer_total(list = dealers_cards)}")
        if dealer_total(list= dealers_cards) > 21:
                print ("Dealer Bust")
        elif dealer_total(list= dealers_cards) == 21 and len(dealers_cards) == 2:
            print("Dealer got Black Jack")
        
        if dealer_total(list= dealers_cards) > 21 and player_total(list= player_cards) > 21:
            print("The Dealer and Player Lose")
        elif dealer_total(list= dealers_cards) > 21:
                print ("WINNER: Player wins")
        elif player_total(list= player_cards) > 21:
            print("WINNER: Dealer Wins")
        elif player_total(list= player_cards) == dealer_total(list= dealers_cards):
            print("looks like it's a Draw")
        elif dealer_total(list= dealers_cards) > player_total(list= player_cards):
            print("WINNER: Dealer Wins")
        elif player_total(list= player_cards) > dealer_total(list= dealers_cards):
            print("WINNER: Player Wins")
        start_game = input('Do you want to play Balck Jack again. Type "y" to play or "n" for quit: ').lower()
        if start_game != "y":
            print("Good Bye")   

play_black_jack()