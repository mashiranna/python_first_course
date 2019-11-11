"""
Число Армстронга - це таке натуральне число, яке дорівнює сумі своїх цифр, зведених в ступінь, рівну кількості його цифр.
Знайти всі такі числа від 1 до n, де n вводиться на вимогу з клавіатури.
"""
import re
re_integer = re.compile("^\d+$")
k = 1
q = True

def validator_1(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def validator_2(prompt):
    number = int(validator_1(re_integer, prompt))
    while number<=0:
        number = int(validator_1(re_integer, prompt))
    return number

def armst(number):
    global k
    sum = 0
    List = list(str(k))
    L = len(List)
    for i in List:
        sum += (int(i) ** L)
    if k == sum:
        print(str(sum) + " є числом Армстронга")
    k += 1
    return k

while q != '-':
    number = validator_2('Enter integer > 0: ')
    while k <= number:
        armst(number)
    k = 1
    q = input("Press <<->> for exit or any button(s) to continue:")