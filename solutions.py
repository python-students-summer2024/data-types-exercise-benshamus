"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    total_sales = float(input("total sales: "))
    profit = total_sales * 0.23
    print(f"Profit: ${profit:.2f}")

calculate_profit()

def calculate_quotient_and_remainder():
    integer_1 = int(input("Enter number #1: "))
    integer_2 = int(input("Enter number #2: "))
    quotient = integer_1 // integer_2
    remainder = integer_1 % integer_2
    print(f"{integer_2} goes into {integer_1} a total of {quotient} times with a remainder of {remainder}")

calculate_quotient_and_remainder()
""" 
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
"""


def calculate_miles_per_gallon():
    miles = input("Enter miles driven")    
    gas = input("Enter gallons of gas")
    mpg = miles / gas
    print(f"Miles driven: {miles}")    
    print(f"Gas used (gallons): {gas}")
    print(f"Miles per gallon: {mpg}")

calculate_miles_per_gallon()
"""
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
"""


def align_text():
    price_1 = float(input("Enter price #1: "))
    price_2 = float(input("Enter price #2: "))
    price_3 = float(input("Enter price #3: "))
    print("/nHere are your prices!/n")
    print(f"Price #1: ${price_1:10.2f}")
    print(f"Price #2: ${price_2:10.2f}")
    print(f"Price #3: ${price_3:10.2f}")

align_text()

"""
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
