#!/usr/bin/env python3

# Created by: maliksalem1
# Created on: Oct 2022
# This program sees if you guess the right number

import random


def main():
    # This function sees if you guessed right or wrong
    loop_counter = 0

    # Input, Process and Output
    while True:
        guessed_number_string = input("Enter the number between 0-9: ")
        print("")
        try:
            guessed_number_int = int(guessed_number_string)
            random_variable = random.randint(0, 9)
            if guessed_number_int == random_variable:
                print("You guessed right.")
                break
            else:
                print("You guessed wrong, try again.\n")
        except ValueError:
            print("That is not an integer, try again.\n")

    print("\nDone.")


if __name__ == "__main__":
    main()
