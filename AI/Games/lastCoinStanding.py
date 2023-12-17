import random

#initial number of coins in the pile
coins = 20

#players
players = ["Player 1", "Player 2"]

#maximum number of coins that can be removed on each turn
max_coins = 3

#function to get the number of coins to remove on each turn
def get_num_coins():
    #loop for input
    while True:
        num = input("Enter the number of coins to remove (1-3): ")
        #if valid input 
        if num.isdigit() and int(num) <= max_coins and int(num) > 0:
            return int(num)
        #if not a valid input
        print("Invalid input. Please enter a number between 1 and 3.")

#random turn 
current_player = random.choice(players)
#the main game loop
while coins > 0:
    print(f"{current_player}'s turn:")
    #taking numbers of coins removed by a player  
    num_coins = get_num_coins()
    #subtracted from the coin pile
    coins -= num_coins
    print(f"{num_coins} coins removed from the pile. {coins} coins left.\n")
    if coins == 0:
        #no more coins to be removed from the pile now so the last player wins
        print(f"{current_player} wins!")
        break
    #changing the turns 
    current_player = players[1] if current_player == players[0] else players[0]