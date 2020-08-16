""" Counts the execution time """
import sys
import os
from time import time
import importlib

from details import details
from format_time import format_time

def main():
    """
    Calculates the execution time
    """
    start = time()

    # Imports Module Sent as a argument
    module_name = os.path.splitext(sys.argv[1])[0]
    my_mod = importlib.import_module(module_name)

    # Calling main function of imported module
    my_mod.main()

    # Prints Compiler Details & Execution Time of Method
    print(f'\n{details()}')
    execution_time = time() - start
    print(f'Executing Module: {sys.argv[1]}\n'
          f'Total Time of execution = {execution_time} ({format_time(execution_time)})')

if __name__ == "__main__":
    main()
