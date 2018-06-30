"""
TAIL END

Usage:
    tail_end AGE LIFE COUNT UNIT

age in years
life expected life in years
count number of time you perform "something"
unit of "something"  (days_by_week, days_by_month, days_by_year, etc)

"""

import sys
from docopt import docopt

DAYS_IN_YEAR = 365
DAYS_IN_WEEK = 7
WEEKS_IN_YEAR = round(DAYS_IN_YEAR / DAYS_IN_WEEK)
MONTHS = 12
HOURS = 24


# age in years
# life expected life in years
# count number of time you perform "something"
# unit of "something"  (days_by_week, days_by_month, days_by_year, etc)

to_days = lambda x: x * DAYS_IN_YEAR
to_weeks = lambda x: x * WEEKS_IN_YEAR
to_months = lambda x: x * MONTHS
to_hours = lambda x: x * DAYS_IN_YEAR * HOURS
to_years = lambda x: x

def get_convertion_func(unit):
    target_func = "to_" + unit.lower()
    for k, v in globals().items():
        if k == target_func and callable(v):
            return v
    else:
        print("unit not supported")


def main(args):
    age = int(args['AGE'])
    life = int(args['LIFE'])
    count = int(args['COUNT'])
    unit = args['UNIT']
    wasted_time = age
    remaning_time = life - wasted_time
    result_unit, unit_calc = unit.split("_by_")
    f = get_convertion_func(unit_calc)
    remaining_count = f(remaning_time) * count
    g = get_convertion_func(result_unit)
    total_count = life * count
    wasted_count = total_count - remaining_count
    print("you have {} {} out of {} {} more chances".format(remaining_count, result_unit, total_count, result_unit))
    print("you have consumed {}%".format(wasted_count * 100 / total_count))
    print("Remaining {}%".format(remaining_count * 100 / total_count))
if __name__ == "__main__":
    arguments = docopt(__doc__, version='Naval Fate 2.0')
    sys.exit(main(arguments))