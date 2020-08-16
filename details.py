""" Program Prints the Compiler Details for Respective Virtual Environments """
import sys
from datetime import datetime as dt

def details():
    """ Return the Compiler Details """
    version_details = sys.version.split("\n")
    try:
        compiler = version_details[1][1:-1]
    except IndexError:
        compiler = "Default"
    date = dt.now().strftime('%A, %d-%b-%Y %I:%M:%S %p')
    return f"Date: {date}\nPython Version: {version_details[0]}\nCompiler: {compiler}"

def main():
    """ Main Function Prints the Compiler Details """
    print(f'\n{details()}\n')

if __name__ == "__main__":
    main()
