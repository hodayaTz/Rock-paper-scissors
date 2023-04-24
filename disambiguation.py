from random import choice as Choice

OPTIONS = ["Rock🪨", "Paper📃", "Scissors✂️"]

# The optional pairs
PAIRS = [
    (OPTIONS[0], OPTIONS[1]),
    (OPTIONS[1], OPTIONS[2]),
    (OPTIONS[2], OPTIONS[0])
]


def rand_choice():
    return Choice(OPTIONS)


def get_winner(choices):
    """
    Returns the game result of the players
    """
    ch_list = list(choices.items())
    if ch_list[0][1] == ch_list[1][1]:
        print("The result of the game is a draw:)")
        return 0
    return ch_list[1][0] if (ch_list[0][1], ch_list[1][1]) in PAIRS else ch_list[0][0]


def print_options():
    print("Enter your choice:")
    for i in range(len(OPTIONS)): print(i+1," for ", OPTIONS[i])
   
   
def get_player_choice():
    """
    Get player selection by input,
    If the input is invalid, the computer will make a selection.
    """
    print_options()
    try :
        player_choice = int(input()) -1
        return OPTIONS[player_choice]
    except (ValueError, IndexError):
        print("Your choice is invalid, The computer will choose for you.")
        return rand_choice()


def get_choices(names):
    """
    Provides each player's choice
    :names: List with player's names 
    :return: Dict with {name: choice} for each player
    """
    players_dict = {}
    for name in names:
        is_computer = input(name + ' Do you want the computer to choose for you?(y/n)').lower()
        choice = rand_choice() if is_computer.startswith('y') else get_player_choice()
        players_dict[name] = choice
    return players_dict


def main():
    name1 = input("Enter the name of the first player: \n")
    name2 = input("Enter the name of the second player: \n")
    players_names = [name1, name2]
    answer = 'yes'
    players_choice = {}
    
    while answer.lower().startswith('y'):
        
        players_choice = get_choices(players_names)
        for name, choice in players_choice.items():
            print(name , ": " ,choice)
        winner = get_winner(players_choice)
        if winner:
            print("Congrats! " + winner + " is the winner!!")
        
        answer = input('Do you want to play again?(y/n) \n')


if __name__ == '__main__':
    main()
