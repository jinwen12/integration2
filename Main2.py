"""A program integrates my knowledge about python.

__author__ = Jinyuan Piao"""


def total():
    """
    Calculate total of numbers that user input.
    :return:
    """
    x = True
    while x:
        try:

            number = float(input(
                "Enter your numbers. Enter 0 if you finish entering all the "
                "numbers:"))
            x = 1
            answer = 0
            while x > 0:
                if number > 0:
                    answer += number
                    number = float(input())
                    x += 1
                else:
                    x = 0
            print("The answer is:", answer)
            x = False
        except ValueError:
            print("Please enter a numerical number.")


def purchase():
    """
    Get prices of two items and payment from user input then calculate
    changes.
    :return:
    """
    x = True
    while x:
        try:
            # Get the price of the first item
            price_one = float(input("  Enter the price of the first item:"))
            # Get the price of the second item
            price_two = float(input("  Enter the price of the second item:"))
            # Get the payment amount
            payment = float(input("  Enter your payment: "))
            difference = payment - price_one - price_two
            # Determine if customer still owes
            if difference < 0:
                print(" You still owe ${:,.2f}".format(-difference))

            # or if change is owed
            if difference == 0 or difference > 0:
                print(" Thank you, your change is ${:,.2f}".
                      format(difference))
            x = False

        except ValueError:
            print("Please enter numerical numbers")


def circle_area(radius):
    """
    Calculate area of a circle and return it.
    :param radius:user_input
    :return:area
    """
    import math
    area = math.pi * radius ** 2
    return format(area, '.2f')


def get_area():
    """
    Get a radius from user and output area of the circle.
    :return:
    """
    x = True
    while x:
        try:
            user_input = float(input("  Enter the radius of the circle:"))
            circle_area(user_input)
            print("  The area of the circle is: ", circle_area(user_input))
            x = False
        except ValueError:
            print("Please enter a numerical number.")


def main():
    """
    Greet users, tell the users how to use this program, and get
    input.
    :return:
    """
    print("Welcome to my Integration Project!")
    continue_program = True
    while continue_program:
        print("Enter the choice you would like to use:")
        print("  1.Find the sum of the numbers you entered.")
        print("  2.Calculate the change when you buy two items.")
        print("  3.Calculate the area of a circle.")
        print("  4.Enter 4 to quit.")
        user_choice = input("Enter your choice: ")
        if user_choice == '1':
            total()
        elif user_choice == '2':
            purchase()
        elif user_choice == '3':
            get_area()
        elif user_choice == '4':
            continue_program = False
            print("   Thank you for using! See you!")
        else:
            print("   Please enter 1, 2, 3, or 4.")


main()
