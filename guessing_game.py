import math
from random import randint


def create_random_number_list(list_lenght:int, scope_start:int, scope_end:int):
    random_number_list = []
    for element in range(list_lenght):
        random_number_list.append(randint(scope_start, scope_end))
    return random_number_list, scope_start, scope_end

def game_logic(list_lenght:int, scope_start:int, scope_end:int):
    random_numbers, scope_start, scope_end = create_random_number_list(list_lenght, scope_start, scope_end)
    for index in range(len(random_numbers)):
        user_number = int(input(f"Enter an integer from {scope_start} to {scope_end}: "))
        while random_numbers[index] != user_number:
            number_to_compare = random_numbers[index]
            if user_number < number_to_compare:
                print("guess is low")
            elif user_number > number_to_compare:
                print("guess is high")
            else:
                break
            user_number = int(input(f"Enter an integer from {scope_start} to {scope_end}: "))
        print("you guessed it!")

