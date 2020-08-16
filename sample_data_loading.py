""" Sample Data Loading Program """
# pylint: disable = W1401

import os
import pandas as pd

def load(files_list):
    """ Function Collects Data From Local Using Pandas """
    total_chars = 0
    for file in files_list:
        dataframe = pd.read_csv(file)
        for col in dataframe:
            for cell in dataframe[col]:
                total_chars += len(str(cell))
    return total_chars

def main():
    """ Main Function """
    lof = os.listdir(".\Data Samples")
    load([os.path.join(os.getcwd(), 'Data Samples', file) for file in lof])
    # Returns the Total Number of Chars in CSVs \
    # But we are Just Concerned About Loading, not Printing.

if __name__ == "__main__":
    main()
