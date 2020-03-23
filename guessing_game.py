import math
from random import randint


def create_random_number_list(list_lenght:int, scope_start:int, scope_end:int):
    random_number_list = []
    for element in range(list_lenght):
        random_number_list.append(randint(scope_start, scope_end))
    return random_number_list, scope_start, scope_end


def handle_user_input(scope_start:int, scope_end:int):
    return int(input(f"Enter an integer from {scope_start} to {scope_end}: "))


def handle_number_input_comparison(user_number:int, number_to_compare:int):
    if user_number < number_to_compare:
        print("guess is low")
    elif user_number > number_to_compare:
        print("guess is high")
    else:
        return False

def game_logic(list_lenght:int, scope_start:int, scope_end:int):
    random_numbers, scope_start, scope_end = create_random_number_list(list_lenght, scope_start, scope_end)
    for index in range(len(random_numbers)):
        user_number = handle_user_input(scope_start, scope_end)
        while random_numbers[index] != user_number:
            number_to_compare = random_numbers[index]
            comparison_result = handle_number_input_comparison(user_number, number_to_compare)
            user_number = handle_user_input(scope_start, scope_end)
            if comparison_result == False:
                break
        print("you guessed it!")



def run_application():
    game_logic(10, 1, 99)
    game_logic(10, 1, 49)

# for i in range(10):
#     g = int(input("Enter an integer from 1 to 99: ")) 
#     while a[i] != g:
#         if g < a[i]:
#             print("guess is low")
#             g = int(input("Enter an integer from 1 to 99: "))
#         elif g > a[i]:
#             print("guess is high")
#             g = int(input("Enter an integer from 1 to 99: "))
#         else:
#             break
#     print("you guessed it!")


# for i in range(10):
#     g = int(input("Enter an integer from 1 to 49: "))
#     while b[i] != g:
#         if g < b[i]:
#             print("guess is low")
#             g = int(input("Enter an integer from 1 to 49: "))
#         elif g > b[i]:
#             print("guess is high")
#             g = int(input("Enter an integer from 1 to 49: "))
#         else:
#             break
#     print("you guessed it!")
if __name__ == "__main__":
    run_application()