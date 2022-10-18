#!/usr/bin/env python3

# Created By: Peter Sobowale
# Date: October 14, 2022
# This program asks the user for a number (1-12)
# and associates the number with the corresponding
# month
from select import select


def main():
    # Get month user input
    user_month = int(input("Enter a number for a month (1-12): "))

    # check and select which case to run based on user input
    match user_month:
        case 1:
            print("1 is January")
        case 2:
            print("2 is February")
        case 3:
            print("3 is March")
        case 4:
            print("4 is April")
        case 5:
            print("5 is May")
        case 6:
            print("6 is June")
        case 7:
            print("7 is July")
        case 8:
            print("8 is August")
        case 9:
            print("9 is September")
        case 10:
            print("10 is October")
        case 11:
            print("11 is November")
        case 12:
            print("12 is December")
        case _:
            print(str(user_month) + " doesn't correspond to any month")


if __name__ == "__main__":
    main()
