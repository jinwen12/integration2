def total():
    number = float(input(" Enter your number. Enter 0 if you finish entering all the numbers:"))
    x = 1
    answer = 0
    while x > 0:
        if number > 0:
            answer = answer + number
            number = float(input())
            x += 1
        else:
            x = 0
    print("The answer is:",answer)
def purchase():
    # Get the price of the first item
    price1 = float(input("  Enter the price of the first item: "))
    # Get the price of the second item
    price2 = float(input("  Enter the price of the second item: "))
    # Get the payment amount
    payment = float(input("  Enter your payment: "))
    difference = payment - price1 - price2
    # Determine if customer still owes
    if difference < 0:
        print(" You still owe ${:,.2f}".format(-difference))

    # or if change is owed
    if difference == 0 or difference > 0:
        print(" Thank you, your change is ${:,.2f}".format(difference))
def circleArea(radius):
    import math
    area=math.pi*radius**2
    return(format(area,'.2f'))
def area():
    userinput=float(input("  Enter the radius of the circle:"))
    circleArea(userinput)
    print("  The area of the circle is: ",circleArea(userinput))
def main():
    print("Welcome to my Integration Project!")
    continueProgram=True
    while continueProgram:
        print("Enter the choice you would like to use:")
        print("  1.Find the sum of the numbers you entered.")
        print("  2.Calculate the change when you buy two items.")
        print("  3.Calculate the area of a circle.")
        print("  4.Enter 4 to quit.")
        userChoice=float(input("Enter your choice: "))
        if userChoice==1:
            total()
        elif userChoice==2:
            purchase()
        elif userChoice==3:
            area()
        elif userChoice==4:
            continueProgram=False
            print("   Thank you for using! See you!")
        else:
            print("   Please enter an interger from 1 to 4.")
main()
