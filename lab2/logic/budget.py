import datetime


def is_number_correct(total):
    """checks whether the number is positive"""
    if int(total) < 0:
        return None
    return True


class Budget:
    budget_holder = {}

    def __init__(self, total, owner, budget_holder=None):
        if not(is_number_correct(total)):
            raise ValueError("Incorrect total value!")
        self.total = int(total)
        self.owner = owner
        if budget_holder is None:
            self.budget_holder[datetime.datetime.now()] = total
        else:
            self.budget_holder = budget_holder

    def dec_total(self, dif):
        """reduce the total amount to a certain size"""
        if not (is_number_correct(dif)):
            raise ValueError("Incorrect total value!")
        self.total -= int(dif)
        self.budget_holder[datetime.datetime.now()] = self.total

    def inc_total(self, dif):
        """increase the total amount to a certain size"""
        if not(is_number_correct(dif)):
            raise ValueError("Incorrect total value!")
        self.total += int(dif)
        self.budget_holder[datetime.datetime.now()] = self.total

    def get_total(self):
        """get the total"""
        return self.total

    def get_owner(self):
        """"get the owner"""
        return self.owner

    def get_statistic(self):
        """"get statistic dictionary"""
        return self.budget_holder

