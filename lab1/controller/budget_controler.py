from custom_io import input_output
from logic import budget


def program_cycle():
    """init program cycle"""
    name = input_output.input_owner()
    input_output.say_hello(name)
    user = start_init(input_output.start_init(), name)
    program_cycle_aux(user)


def start_init(total, name):
    """create user budget instance"""
    user = budget.Budget(total, name)
    return user


def program_cycle_aux(user):
    """program cycle helper"""
    while True:
        input_output.init_menu()
        number = int(input("Select menu item:\n"))
        if is_menu_item_correct(number):
            menu_decider(number, user)
        elif number == 6:
            break
        else:
            print("Try once more!")


def is_menu_item_correct(number):
    """check number"""
    if 0 < number < 6:
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


if __name__ == '__main__':
    program_cycle()
