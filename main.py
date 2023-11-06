from sympy import sympify
import colorama
from colorama import just_fix_windows_console, init, Fore, Back,Style
just_fix_windows_console()
init()

language = input("Choose language (en, ru): ")
if language == "en":
    num1 = str(input("Enter the first number: "))
    action = input("+ - / *: ")
    num2 = str(input("Enter a second number: "))
    try:
        print(sympify(num1 + action + num2))
    except (NameError, SyntaxError):
        print(Fore.RED + "You have entered an incorrect data type!")
elif language == "ru":
    num1 = str(input("Введите первое число: "))
    action = input("+ - / *: ")
    num2 = str(input("Введите второе число: "))
    try:
        print(sympify(num1 + action + num2))
    except (NameError, SyntaxError):
        print(Fore.RED + "Вы ввели направильный тип данных!")
else:
    print("Incorrect input. Only " + Fore.BLUE +"en and ru "+ Fore.RESET + "are available")
    language = input("Choose language (en, ru): ")
    if language == "en":
        num1 = str(input("Enter the first number: "))
        action = input("+ - / *: ")
        num2 = str(input("Enter a second number: "))
        try:
            print(sympify(num1 + action + num2))
        except (NameError, SyntaxError):
            print(Fore.RED + "You have entered an incorrect data type!")
    elif language == "ru":
        num1 = str(input("Введите первое число: "))
        action = input("+ - / *: ")
        num2 = str(input("Введите второе число: "))
        try:
            print(sympify(num1 + action + num2))
        except (NameError, SyntaxError):
            print(Fore.RED + "Вы ввели направильный тип данных!")
