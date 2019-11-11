"""
Oбчислення конкретної функції, в залежності від введеного значення х.
"""
import re
q = True

re_x = re.compile("^[-+]?\d+\.?\d*$")

def validator_1(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def validator_2(prompt):
    x = int(validator_1(re_x, prompt))
    if x > 3:
        y = -3 * x + 9
        print(y)
    else:
        y = x * x * x / (x * x + 8)
        print(y)
    return x

while q != '-':
    x = validator_2("Enter x: ")
    q = input("Press <<->> for exit or any button(s) to continue:")



