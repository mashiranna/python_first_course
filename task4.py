""""
 Обчислити
"""

import re
re_n = re.compile("^\d+$")
re_x = re.compile("^\d+\.?\d*$")
q = True

def validator_1(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def validator_2(prompt):
    n = int(validator_1(re_n, prompt))
    while n < 1 :
        n = int(validator_1(re_n, prompt))
    return n

def validator_3(prompt):
    x = float(validator_1(re_x, prompt))
    return x

while q != '-':
    summa = 0
    n = validator_2("Enter n: ")
    x = validator_3("Enter x: ")
    for i in range(1, n+1):
        summa += (x+i)**2
    print(float(summa))
    q = input("Press <<->> for exit or any button(s) to continue:")
