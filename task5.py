"""
Дано ціле число N(>0). Якщо воно є ступенем числа 3, то вивести True, якщо ні - вивести False.
"""
import re
import math

re_n = re.compile("^\d+$")
q = True

def validator_1(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def validator_2(prompt):
    n = int(validator_1(re_n, prompt))
    while n <= 0 :
        n = int(validator_1(re_n, prompt))
    return n

while q != '-':
    i = 0
    n = validator_2("Enter n > 0: ")
    exists = False
    while i < n and not exists:
        if 3 ** i == n:
            exists = True
        else:
            i = i + 1
    if exists:
        print(True)
    else:
        print(False)
    q = input("Press <<->> for exit or any button(s) to continue:")