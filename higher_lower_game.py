import random
from replit import clear
from higher_lower_data import data
from higher_lower_art import logo, vs

def get_random_account(list_data):
    
    """This funciton randomly picks an element from a list"""
    
    account_chosen_dict = random.choice(list_data)
    return account_chosen_dict

def get_account_info(account_dict):
    
    """This function takes account dictionary as input, returns name, description, and country"""
    
    name = account_dict['name']
    description = account_dict['description']
    country = account_dict['country']
    return f'{name}, a {description}, from {country}'


def get_name(account_chosen_dict):
    
    """This function takes account dictionary as input and returns name info""" 
    
    return account_chosen_dict['name']

def compare_a_and_b(player_choice, account_chosen_a_dict, account_chosen_b_dict):
    
    """This function compare the amount of followers, if a > b, then player should choose a
    if b > a, then player should choose b, return boolean (True or False)"""
    
    a_num_followers = account_chosen_a_dict['follower_count']
    b_num_followers = account_chosen_b_dict['follower_count']
    
    # If a follower is greater than b, player should choose a, vice versa
    if (a_num_followers > b_num_followers and player_choice == 'a') or (a_num_followers < b_num_followers and player_choice == 'b') :
        return True
    elif (a_num_followers > b_num_followers and player_choice == 'b') or (a_num_followers < b_num_followers and player_choice == 'a'):
        return False

def play_game():

    """This function contains the game logic"""
    score = 0
    print(logo)
    
    # An empty list that stores all the already picked account
    already_pick_name = []
    account_chosen_a_dict = get_random_account(list_data = data)
    already_pick_name.append(get_name(account_chosen_dict = account_chosen_a_dict))


    end_of_game = False
    while not end_of_game:
        account_chosen_b_dict = get_random_account(list_data = data)

        # if account_chosen_b_dict is same as account_chosen_a_dict, we we need to reselect account_chosen_b_dict
        # if newly chosen one is already in the "already_pick_name" list, we also need to reselect, because we do not want something selected before appear again 
        # if account_chosen_b_dict is completely new, then we append this new info to the list
        
        if account_chosen_a_dict == account_chosen_b_dict:
            account_chosen_b_dict = get_random_account(list_data = data)
        elif account_chosen_b_dict['name'] in already_pick_name:
            account_chosen_b_dict = get_random_account(list_data = data)
        else:
            already_pick_name.append(get_name(account_chosen_dict = account_chosen_b_dict))

        print(f'Compare A: {get_account_info( account_dict = account_chosen_a_dict)}')
        print(vs)
        print(f'Compare B: {get_account_info( account_dict = account_chosen_b_dict)}')

        player_choice = input("Who has more followers? Type 'A' or 'B' ").lower()
        is_correct = compare_a_and_b(player_choice = player_choice, account_chosen_a_dict = account_chosen_a_dict, account_chosen_b_dict = account_chosen_b_dict)

        clear()
        print(logo)

        if is_correct == True:
            score += 1
            # Update the "account_chosen_a_dict" with "account_chosen_b_dict"
            account_chosen_a_dict = account_chosen_b_dict
            print(f"You got it, current score: {score}")
            # print(already_pick_account)
        else:
            end_of_game = True
            print(f"Sorry, That's wrong answer, your final score: {score}")
            print(already_pick_name)
            
while input("Do you want to play higher lower game? Type 'Y' or 'N' ").lower() == 'y':        
    play_game()