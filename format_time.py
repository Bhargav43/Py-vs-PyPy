""" Module to Convert the Seconds to Respective Time Units """
# pylint: disable = R1705

import sys

def format_time(seconds):
    """ Converts Seconds to Suitable Unit of Time and Returns Sting with Value and Unit """
    micro, milli, mins, hours, index = 0, 0, 0, 0, 0
    units = {-2: 'Microsecond', -1: 'Millisecond', 0 : 'Seconds', 1 : 'Minutes', 2 : 'Hours'}

    # Converting to Milliseconds
    if seconds < 1:
        milli = seconds * 1000
        index = -1
        # Converting to Microseconds
        if milli < 1:
            micro = milli * 1000
            index = -2

    # Dividing Minutes from Total Seconds
    while seconds >= 60:
        seconds -= 60
        mins += 1
        index = 1

    # Dividing Hours from Total Minutes
    while mins >= 60:
        mins -= 60
        hours += 1
        index = 2
    if index == 2: # Hours
        return f'{hours}:{mins:02d}:{seconds:02d} {units[index]}'
    elif index == 1: # Minutes
        return f'{mins:2d}:{seconds:02d} {units[index]}'
    elif index == 0: # Seconds
        return f'{seconds:.2f} {units[index]}'
    elif index == -1: # Milliseconds
        return f'{milli:.2f} {units[index]}'
    else:# Microseconds
        return f'{micro:.2f} {units[index]}'


def main():
    """ Main Function with Sample Call """
    if len(sys.argv)>1:
        print(f'{sys.argv[1]} Seconds = ', format_time(int(sys.argv[1])))
    else:
        print('21,600 Seconds = ', format_time(21600))

if __name__ == '__main__':
    main()
