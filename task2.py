"""
Перевірка правильності дати, введеної з клавіатури
"""
import re
q = True

re_day = re.compile("^\d+$")
re_month = re.compile("^\d+$")

def validator_1(pattern, promt):
    text = input(promt)
    while not bool(pattern.match(text)):
        text = input(promt)
    return text

def validator_2(prompt):
    day = int(validator_1(re_day, prompt))
    while (day<1) or (day>32):
        day = int(validator_1(re_day, prompt))
    return day

def validator_3(prompt):
    month = int(validator_1(re_month, prompt))
    while (month < 1) or (month > 12):
        month = int(validator_1(re_month, prompt))
    return month

while q != '-':
    day = validator_2("Enter day: ")
    month = validator_3("Enter month: ")
    print("Correctly entered data: day: " + str(day)  + ", month: " + str(month))
    q = input("Press <<->> for exit or any button(s) to continue:")
