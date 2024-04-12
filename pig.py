import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit(): #checking if the string is a valid number before converting it to an int
        players = int(players) #converting to int 
        if 2 <= players <= 4: #makes sure the amount of players is 2-4 people 
            break
        else:
            print("Must be between 2 - 4 people")
    else:
        print("Invalid, try again.")

max_score = 50
#this list will change size based on the number of players -> range function loops the number of players times that we have.  'players' is an int 
player_scores = [0 for _ in range(players)] 

while max(player_scores) < max_score:

    for player_idx in range(players): #looping over each player so they each get a turn
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is: ", player_scores[player_idx], "\n")
        current_score = 0 

        while True: 
            should_roll = input("would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break #if yes is not the answer then we break from the program

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!") #turn is done on one
                current_score = 0
                break
            else: 
                current_score += value #if one isn't rolled then the process continues after printing the value of what the player rolled and adds it to their streak value.
                print("You rolled a: ", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player", winning_idx + 1, "is the winner with a score of:", max_score) #'1' is added here because indexes in python start at 0 and we want to make sure we're going from 1-4, not 0-3