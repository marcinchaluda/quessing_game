import math # import math module
import random # import random module
a = [] # creating an empty list
a.append(random.randint(1, 99)) # add one element to the end of the empty list
a.append(random.randint(1, 99)) # add one element to the end of the empty list
a.append(random.randint(1, 99)) # add one element to the end of the empty list
a.append(random.randint(1, 99)) # add one element to the end of the empty list
a.append(random.randint(1, 99)) # add one element to the end of the empty list
a.append(random.randint(1, 99)) # add one element to the end of the empty list
a.append(random.randint(1, 99)) # add one element to the end of the empty list
a.append(random.randint(1, 99)) # add one element to the end of the empty list
a.append(random.randint(1, 99)) # add one element to the end of the empty list
a.append(random.randint(1, 99)) # add one element to the end of the empty list
for i in range(10): # iterating from 0 to 9 which is the length of the list
    g = int(input("Enter an integer from 1 to 99: ")) # convert user input as integer and assign it to a variable 
    while a[i] != g: # looping through consecutive elements in a list until user input is equal to given element
        if g < a[i]: # check if user input is lower than given list element
            print("guess is low") # print hint that given number is lower than user input
            g = int(input("Enter an integer from 1 to 99: ")) # convert user input as integer and assign it to a variable
        elif g > a[i]: # check if user input is higher than given list element
            print("guess is high") # print hint that given number is higher than user input
            g = int(input("Enter an integer from 1 to 99: ")) # convert user input as integer and assign it to a variable
        else: # if above conditions are not met execute below code
            break # exit from loop even if loop did not finish its working 
    print("you guessed it!") # print information that your input is equal to given element from a list

b = []# creating an empty list
b.append(random.randint(1, 49))# add one element to the end of the empty list
b.append(random.randint(1, 49))# add one element to the end of the empty list
b.append(random.randint(1, 49))# add one element to the end of the empty list
b.append(random.randint(1, 49))# add one element to the end of the empty list
b.append(random.randint(1, 49))# add one element to the end of the empty list
b.append(random.randint(1, 49))# add one element to the end of the empty list
b.append(random.randint(1, 49))# add one element to the end of the empty list
b.append(random.randint(1, 49))# add one element to the end of the empty list
b.append(random.randint(1, 49))# add one element to the end of the empty list
b.append(random.randint(1, 49))# add one element to the end of the empty list
for i in range(10): # iterating from 0 to 9 which is the length of the list
    g = int(input("Enter an integer from 1 to 49: ")) # convert user input as integer and assign it to a variable
    while b[i] != g: # looping through consecutive elements in a list until user input is equal to given element
        if g < b[i]: # check if user input is lower than given list element
            print("guess is low") # print hint that given number is lower than user input
            g = int(input("Enter an integer from 1 to 49: ")) # convert user input as integer and assign it to a variable
        elif g > b[i]: # check if user input is higher than given list element
            print("guess is high") # print hint that given number is higher than user input
            g = int(input("Enter an integer from 1 to 49: ")) # convert user input as integer and assign it to a variable
        else: # if above conditions are not met execute below code
            break # exit from loop even if loop did not finish its working
    print("you guessed it!") # print information that your input is equal to given element from a list
