from random import choice

options = ["Rock🪨", "Paper📃", "Scissors✂️"]

# The optional pairs 
pairs = [
    (options[0], options[1]),
    (options[1], options[2]),
    (options[2], options[0])
]

def rand_choice():
    """
    rands choice for each player
    """     
    choice1 = choice(options)
    new_opts = list(filter(lambda i: i !=choice1, options))
    choice2 = choice(new_opts)
    
    return choice1, choice2
    
    
def get_winner(*players_choice):
    """
    returns the winner between 2 players
    """
    return 1 if (players_choice[0], players_choice[1]) in pairs else 0
    
def main():
    name1 = input("Enter the name of the first player: \n")
    name2 = input("Enter the name of the second player: \n")
    players_names = [name1, name2]
    answer = 'yes'
    while answer.startswith('y'):
        players_choice = rand_choice()
        for i in range(len(players_names)):
            print(players_names[i]+": "+ players_choice[i])
        winner = get_winner(*players_choice)
        print("congrats! " +players_names[winner] + " is the winner!!")
        answer = input('Do you want to play again?(y/n) \n')
    
if __name__ == '__main__': 
    main()
