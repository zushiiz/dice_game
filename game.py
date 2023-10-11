import random

def roll_dice():
        pull = random.randint(1, 6)
        return pull

def dealer(dealer_points):

    while dealer_points <= 17:
        dealer_roll = roll_dice()
        dealer_points += dealer_roll
        print(f"the dealer pulled {dealer_roll} and has {dealer_points} points")
        if dealer_points > 21:
            print("the dealer got over 21 points the player wins")
            play_again()
    return dealer_points

def player(player_input, player_points):
    while True:

        if player_input == "stop":
             return player_points

        elif player_input == "roll":
            player_roll = roll_dice()
            player_points += player_roll
            print(f"You rolled {player_roll} and you have {player_points} points")

        if player_points > 21:
            print("the player got over 21 points the dealer wins")
            play_again()

        player_input = input("roll again or stop?")

def winner(a, b):

        if b == a:
            print("its a tie!")

        elif a < b <= 21:
            print(f"the dealer has {b} points and player has {a} points dealer is the winner")

        elif b < a <= 21:
            print(f"the dealer has {b} points and player has {a} points player is the winner")

def play_again():
    x = input("want to play again, yes or no:")
    if x == "yes":
        maingame()

    else:
        print("thank you for playing")
        play_again()

def maingame():    
    player_input = input("roll or stop:")

    player_points = 0
    dealer_points = 0

    player_end = player(player_input, player_points)
    dealer_end = dealer(dealer_points)
    
    winner(player_end, dealer_end)

    play_again()

maingame()