#!/usr/bin/env python3

# Created by: Youngjun Kim
# Created on: May 2021
# This program add integers using a while loop


def main():
    # this function add integers using a while loop

    # this is to keep track of hw many times you go through the loop
    loop_counter = 0
    sum = 0

    # input
    integer_as_string = input("Enter an positive integer: ")

    # process & output
    try:
        integer_as_number = int(integer_as_string)
        if integer_as_number > 0:
        
            while loop_counter <= integer_as_number:
                sum = sum + loop_counter
                loop_counter = loop_counter + 1
            print("The sum of all positive numbers is {0}.".format(sum))
    except Exception:
        print("That was not valid input.")

if __name__ == "__main__":
    main()
