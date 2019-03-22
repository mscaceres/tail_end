"""
TAIL END

Usage:
    tail_end AGE LIFE COUNT UNIT

age in years
life expected life in years (or upper limit you plan to stop doing something)
count number of time you perform "something"
unit of "something"  (days_by_week, days_by_month, days_by_years, etc)

"""

import sys
from docopt import docopt
from collections import namedtuple
import shutil
from tick import ColorTick


TERM_COLUMNS, _ = shutil.get_terminal_size()

Opportunities = namedtuple('Opportunities', 'total, wasted, remaining, unit')

DAYS_IN_YEAR = 365
DAYS_IN_WEEK = 7
WEEKS_IN_YEAR = round(DAYS_IN_YEAR / DAYS_IN_WEEK)
MONTHS = 12
HOURS = 24


to_days = lambda x: x * DAYS_IN_YEAR
to_weeks = lambda x: x * WEEKS_IN_YEAR
to_months = lambda x: x * MONTHS
to_hours = lambda x: x * DAYS_IN_YEAR * HOURS
to_years = lambda x: x


def get_convertion_func(unit):
    target_func = "to_" + unit.lower()

    if not target_func.endswith('s'):
        target_func = target_func + 's'

    for name, obj in globals().items():
        if callable(obj) and name == target_func :
            return obj
    else:
        raise ValueError("unit not supported")


def tail_end(time_doing, time_total, times, unit):
    """

    time_doing: integer, time being doing something
    time_total: integer, time expected of being doing something
    times: integer, amount of times doing something
    unit: unit of times
    """
    result_unit, unit_calc = unit.split("_by_")
    f = get_convertion_func(unit_calc)
    time_remaining = time_total - time_doing
    remaining = f(time_remaining) * times
    total = f(time_total) * times
    wasted = total - remaining
    return Opportunities(total, wasted, remaining, result_unit)


class Printer(object):

    def __init__(self, lenght, used_tick, free_tick):
        """
        tick stand for a unit of time
        lenght: amount of character to print per line
        used_tick: character to represent used tick
        free_tick: character to represent remaining tick
        """
        self.ticks_in_line = lenght
        self.used_tick = used_tick
        self.free_tick = free_tick
        self.padding = int((TERM_COLUMNS - self.ticks_in_line) / 2)

    def print(self, wasted, remaining):
        one_liner = self.used_tick * wasted + self.free_tick * remaining
        lines = (one_liner[s:s+self.ticks_in_line] for s in range(0, wasted + remaining, self.ticks_in_line))
        line = ("{:>{width}}".format(line, width=self.padding+len(line)) for line in lines)
        print("\n".join(line))


def main(args):
    try:
        age = int(args['AGE'])
        life = int(args['LIFE'])
        count = int(args['COUNT'])
        unit = args['UNIT']

        chances = tail_end(time_doing=age, time_total=life, times=count, unit=unit)

        red_tick = ColorTick.from_color_string("red", "#")
        green_tick = ColorTick.from_color_string("green", "0")
        p = Printer(10, used_tick=red_tick, free_tick=green_tick)

        print("you have {} {} out of {} {} more chances".format(chances.remaining, chances.unit, chances.total, chances.unit))
        print("you have consumed {}%".format(chances.wasted * 100 / chances.total))
        print("Remaining {}%".format(chances.remaining * 100 / chances.total))

        p.print(chances.wasted, chances.remaining)
        return 0
    except ValueError as e:
        print(e, file=sys.stderr)
        return 1


if __name__ == "__main__":
    arguments = docopt(__doc__, version='0.1')
    sys.exit(main(arguments))
