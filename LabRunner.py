from lab1.controller import budget_controler as lab1
from lab2.controller import budget_controler as lab2


if __name__ == '__main__':
    number = int(input("Chose lab:"))
    if number == 1:
        lab1.program_cycle()
    elif number == 2:
        lab2.program_cycle()
