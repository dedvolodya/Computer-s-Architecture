def input_sum():
    """ask the user to enter the number"""
    input("Input your sum:\n")


def input_owner():
    """ask the user to enter the name"""
    name = input("What is your name?\n")
    return str(name)


def say_hello(name):
    """say hello to user"""
    print("Hello, " + str(name))


def out_statistic(budget_holder):
    """normalize budget dictionary and output it"""
    for key in budget_holder:
        print("Date : " + str(str(key)) + "  Total sum: " + str(budget_holder[key]))


def out_owner(name):
    """output owner"""
    print("Owner of this bill is " + str(name))


def out_total(total):
    """output total budget"""
    print("Total budget: " + str(total))


def start_init():
    """ask user to enter the starting budget"""
    current_budget = input("Please, input your current budget\n")
    return int(current_budget)


def init_menu():
    """output menu"""
    print("1. Decrement my budget.")
    print("2. Increment my budget.")
    print("3. Get my current budget.")
    print("4. Get my budget statistic.")
    print("5. Who am I?")
    print("6. Exit.")
