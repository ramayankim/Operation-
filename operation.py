import operator

import os


ops = { '1': ('+', operator.add), '2': ('-', operator.sub), '3': ('*', operator.mul), '4': ('/', operator.truediv) }


def clear_screen():

os.system('cls' if os.name == 'nt' else 'clear')

while True:

clear_screen()

print("python calculator")

print("=================")

print("\n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division \n5.Exit")

choice = input("Enter Operator: ")


if choice == '5': break

if choice in ops:

n1 = float(input("Enter first number: "))

n2 = float(input("Enter second number: "))

symbol, func = ops[choice]

print(f"{n1} {symbol} {n2} = {func(n1, n2)}")

else:

print("Invalid choice.")

input("\nPress Enter to continue...")