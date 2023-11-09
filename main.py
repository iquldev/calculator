from sympy import sympify
import colorama
from colorama import just_fix_windows_console, init, Fore, Back, Style
just_fix_windows_console()
init()

def calc(mode):
    if mode == "simple":
        num1 = input(messages[0])
        action = input("+ - / *: ")
        num2 = input(messages[1])
        equation = num1 + action + num2
        try:
            print(Fore.YELLOW + str(sympify(equation)) + Fore.RESET)
        except (NameError, SyntaxError):
            print(Fore.RED + messages[2])
        answer = input(messages[3]) or "y"
        if answer == "y":
            calc("simple")
        elif answer == "n":
            print(messages[4])
    elif mode == "advanced":
        equation = sympify(input(messages[6]))
        try:
            print(Fore.YELLOW + str(equation) + Fore.RESET)
        except (NameError, SyntaxError):
            print(Fore.RED + messages[2])
        answer = input(messages[3]) or "y"
        if answer == "y":
            calc("advanced")
        elif answer == "n":
            print(messages[4])

language = input("Choose language (en, ru): ")
while (language != "en", language != "ru"):
    if language == "ru":
        messages = [
            "Введите первое число: ",
            "Введите второе число: ",
            "Вы ввели направильный тип данных!",
            "Продолжить работу? (Y, n): ",
            "Пока!",
            "Выберите режим: ",
            "Введите уравнение: "
        ]
        break
    elif language == "en":
        messages = [
            "Enter the first number: ",
            "Enter a second number: ",
            "You have entered an incorrect data type!",
            "Continue work? (Y, n): ",
            "Bye!",
            "Select the mode: ",
            "Enter the equation: "
        ]
        break
    language = input("Choose language (en, ru): ")

print(Fore.GREEN + '[1] ' + Fore.RESET + 'Simple mode\n' + Fore.GREEN + '[2] ' + Fore.RESET + 'Advanced mode')
mode = input(messages[5])
while (mode != "1", mode != "2"):
    if mode == "1":
        calc("simple")
        break
    elif mode == "2":
        calc("advanced")
        break
    mode = input(messages[5])
