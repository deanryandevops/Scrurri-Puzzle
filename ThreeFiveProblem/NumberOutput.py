number_amount = 100 # maximum number for test

def check_number(number_to_check): # check the number to is inputted in
    number = number_to_check
    three_five_counter = 0
    check_three = number_to_check % 3 # using modulo to get the remainder number of 3
    check_five = number_to_check % 5 # using modulo to get the remainder number of 5

    if check_three == 0: # if zero we don't that there is no remainder so it must match the 3
        number = "Three" # number set to Three
        three_five_counter += 1 # to add counter to allow for the number dividable by 3 and 5

    if check_five == 0:
        number = "Five" # number set to Five
        three_five_counter += 1 # to add counter to allow for the number dividable by 3 and 5

    if three_five_counter == 2: # once this counter is 2 we know that it has gone through 3 and 5
        number = "ThreeFive" # number set to ThreeFive

    return number

def print_number(): # print number
    for number in range(101): # loop through range 0 - 100
        print(check_number(number)) # prints the number




