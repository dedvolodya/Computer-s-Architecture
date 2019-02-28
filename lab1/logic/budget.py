import datetime


def is_number_correct(total):
    if int(total) < 0:
        return None
    return True


class Budget:
    budget_holder = {}

    def __init__(self, total, owner):
        if not(is_number_correct(total)):
            raise ValueError("Incorrect total value!")
        self.total = int(total)
        self.owner = owner
        self.budget_holder[datetime.datetime.now()] = total

    def dec_total(self, dif):
        if not (is_number_correct(dif)):
            raise ValueError("Incorrect total value!")
        self.total -= int(dif)
        self.budget_holder[datetime.datetime.now()] = self.total

    def inc_total(self, dif):
        if not(is_number_correct(dif)):
            raise ValueError("Incorrect total value!")
        self.total += int(dif)
        self.budget_holder[datetime.datetime.now()] = self.total

    def get_total(self):
        return self.total

    def get_owner(self):
        return self.owner

    def get_statistic(self):
        return self.budget_holder
