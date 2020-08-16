""" Program for creating batch file """
# pylint: disable = W1401
import os
import sys

def save_file(filename, value):
    """ Function for saving the text into file """
    with open(filename, "w") as file:
        file.write(value)
    return filename

def create_bat(**kwargs):
    """ Created the Batch File Text for Execution """
    path = os.getcwd()
    if os.path.isfile(os.path.join(path, kwargs['filename'])):
        filename = kwargs['filename']

    if 'args' in kwargs.keys():
        filename += ' ' + ' '.join(kwargs['args'])

    venv = kwargs['venv']

    fulltext = (f'cmd /k "cd .\\{venv["PyPy"]}\Scripts & activate & cd ..\..' +
                f' & python execution_time.py {filename}' +
                f' & cd .\\{venv["PyPy"]}\Scripts & deactivate & cd ..\..' +
                ######
                f' & cd .\\{venv["Python"]}\Scripts & activate & cd ..\..' +
                f' & python execution_time.py {filename}' +
                f' & cd .\\{venv["Python"]}\Scripts & deactivate & cd ..\.."')

    return save_file('Run Me.bat', fulltext)

def main():
    """ Main Function to Consolidate """
    args = sys.argv[1:]
    venvs = {'PyPy': "py36pypy73", 'Python': "python37"}
    if len(args) > 1:
        val = create_bat(filename=args[0], args=args[1:], venv=venvs)
    else:
        val = create_bat(filename=args[0], venv=venvs)
    print(f'Created file "{val}" in the current working directory.')

if __name__ == "__main__":
    main()
