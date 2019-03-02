from lab2.custom_io import input_output
from lab2.logic import budget
from lab2.serialize import common


def init_user():
    while True:
        input_output.init_owner()
        number = int(input("Select menu item:\n"))
        if number == 1:
            user = common.load_user()
            input_output.say_hello(user.get_owner())
            return user
        elif number == 2:
            name = input_output.input_new_owner()
            input_output.say_hello(name)
            return start_budget_init(input_output.start_init(), name)
        elif number == 3:
            return None
        else:
            print("Try once more!")


def program_cycle():
    """init program cycle"""
    user = init_user()
    if user is not None:
        program_cycle_aux(user)


def start_budget_init(total, name):
    """create user budget instance"""
    return budget.Budget(total, name)


def program_cycle_aux(user):
    """program cycle helper"""
    while True:
        input_output.init_menu()
        number = int(input("Select menu item:\n"))
        if is_menu_item_correct(number):
            menu_decider(number, user)
        elif number == 7:
            break
        else:
            print("Try once more!")


def is_menu_item_correct(number):
    """check number"""
    if 0 < number < 7:
        return True
    else:
        return None


def menu_decider(number, user):
    """check typed number and run certain function"""
    if number == 1:
        user.dec_total(input("Enter sum: "))
    elif number == 2:
        user.inc_total(input("Enter sum: "))
    elif number == 3:
        input_output.out_total(user.get_total())
    elif number == 4:
        input_output.out_statistic(user.get_statistic())
    elif number == 5:
        input_output.out_owner(user.get_owner())
    elif number == 6:
        common.save_user(user)
