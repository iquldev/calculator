from sympy import sympify
import colorama
from colorama import just_fix_windows_console, init, Fore, Back, Style
just_fix_windows_console()
init()

def calc():
    num1 = input(num1_message)
    action = input("+ - / *: ")
    num2 = input(num2_message)
    equation = num1 + action + num2
    try:
        print(Fore.YELLOW + str(sympify(equation)) + Fore.RESET)
    except (NameError, SyntaxError):
        print(Fore.RED + error_message)
    answer = input(continue_message) or "y"
    if answer == "y":
        calc()
    elif answer == "n":
        print(farewell)

language = input("Choose language (en, ru): ")
while (language != "en", language != "ru"):
    if language == "ru":
        num1_message = "Введите первое число: "
        num2_message = "Введите второе число: "
        error_message = "Вы ввели направильный тип данных!"
        continue_message = "Продолжить работу? (Y, n): "
        farewell = "Пока!"
        calc()
        break
    elif language == "en":
        num1_message = "Enter the first number: "
        num2_message = "Enter a second number: "
        error_message = "You have entered an incorrect data type!"
        continue_message = "Continue work? (Y, n): "
        farewell = "Bye!"
        calc()
        break
    language = input("Choose language (en, ru): ")
