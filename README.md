<style>
    * {color: #000080;}
    h1.header {color: #2E8B57; font-size: 35; font-family: Palatino Linotype;}
    h1.footer {color: #E2B13C; font-family: Palatino Linotype;}
    h2, h3, h4, h5 {color: #3Cb371; font-family: Palatino Linotype;}
    a:link, a:visited, a:hover, a:active {color: #2778D1; font-size: 16px; font-family: Lucida Console;}
    p.note {color: #FF7F50; font-family: Palatino Linotype;}
</style>

<h1 class="header">Py-vs-PyPy: For PyPy Compiler's Performance Testing</h1>

## What is PyPy?

PyPy is a fast, compliant alternative implementation of Python to [CPython](https://github.com/python/cpython). Python programs relatively runs faster on PyPy due to the Just-In-Time (JIT) Compiler. Programs might end up taking less space than they do in CPython. It is mostly compatible with all the popular existing python libraries. It was a new feature called [Stackless](https://www.pypy.org/features.html#stackless) which provides micro-threading for massive consurrency. For info and downloading, goto [pypy.org](https://www.pypy.org/).

## What is Virtual Environment?
Python applications often make use of third-party modules which are developed by individuals and registered at [PyPI](https://pypi.org/). Not all modules are required by all applications. Also, different applications might require different versions of modules. Hence Virtual Environments come into picture.

There are more than one module to create virtual environments in Python.
Standard Libraries: [venv](https://docs.python.org/3/library/venv.html), pyvenv (Deprecated in Python 3.6).
Third-party Libraries: [virtualenv](https://pypi.org/project/virtualenv/), [pyenv](https://pypi.org/project/pyenv/), [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) (Plugin), [virtualenvwrapper](https://pypi.org/project/virtualenvwrapper/), [pyenv-virtualenvwrapper](https://github.com/pyenv/pyenv-virtualenvwrapper) (Plugin), [pipenv](https://pypi.org/project/pipenv/).

For more info on these, click on individual names or checkout the [Stack Overflow](https://stackoverflow.com/a/41573588/9207580) answer by Mr.Flimm.

### Creating Virtual Environments:
I wish to create 2 virtual environments as follows:

1. **python37** - Virtual Environment with Python 3.7.7 Default Compiler.
```
python -m virtualenv python37 -p ".\Portable Python-3.7.7 x64\App\Python\python.exe"
```
This created Virtual Environment python37 and it's folder.

2. **pypy36** - Virtual Environment with Python 3.6 with PyPy 7.3 Compiler.
```
python -m virtualenv py36pypy73 -p ".\pypy3.6-v7.3.1-win32\pypy3.exe"
```
This created Virtual Environment py36pypy73 and it's folder.

### To Install Numpy & Pandas Windows Binaries in PyPy Virtual Environment:
I've downloaded and placed the binaries in [.\pypy3.6-v7.3.1-win32\]()
```
Path\to\project\directory> .\virtualenv_name\Scripts\activate
(virtualenv_name) Path\to\project\directory> pypy -m pip install ".\pypy3.6-v7.3.1-win32\numpy-1.18.5+vanilla-pp36-pypy36_pp73-win32.whl"
(virtualenv_name) Path\to\project\directory> pypy -m pip install ".\pypy3.6-v7.3.1-win32\pandas-1.0.5-pp36-pypy36_pp73-win32.whl"
```
<p class="note">Note: If you are downloading the whole [Py-vs-PyPy]() repo to local, you won't need to create virtual environments (or) install packages. But kindly note that due to the portable versions of Python and PyPy, and their Virtual Environment Files, the size of this repo would be high (600+ MB).</p>

### Python Scripts

Sno. | Module Name | Description | Basic Syntax
----:|:-----------:|:------------|:------------
1 | create_batch.py | Creates a Batch File (Run Me.bat) for running the specified program using both Python and PyPy Virtual Environments, and calculating the execution time of both. This is the user module of this application. | python create_batch.py program.py
2 | details.py | Prints the Compiler details of working console. | python details.py
3 | execution_time.py | Calculates the execution time of the program name sent as argument to function. Also calls details.py for compiler details. | python execution_time.py program.py
4 | format_time.py | Formats time (seconds) into respective units: Microseconds/Milliseconds/Seconds/Minutes/Hours. | python format_time.py [No. of Seconds]
5 | sample_data_loading.py | Sample program which processes data using Pandas Module but prints nothing as we are concerned about execution time. | python sample_data_loading.py
6 | sample_waiting_prog.py | Sample program which sleeps for 10 seconds. | python sample_waiting_prog.py

### Usage
#### 1. Creating the Batch File
Open Command Prompt at the project location and run the following, without activating any virtual environments.
1. ```
Path\to\project\directory> python create_batch.py sample_waiting_prog.py
```

##### _(OR)_

2. ```
Path\to\project\directory> python create_batch.py sample_data_loading.py
```

This creates "Run Me.bat" file in the directory which when ran, calculates the execution time of module "sample_waiting_prog.py" or "sample_data_loading.py" in both Python 3.7 and Python3.6 PyPy 7.3 Environments.

#### 2. Running the Batch File
Run the batch file "Run Me.bat" which got created and you see something like this:
##### Output of `sample_waiting_prog.py` 's Batch File:
```
Date: Sunday, 16-Aug-2020 09:55:02 PM
Python Version: 3.6.9 (2ad108f17bdb, Apr 07 2020, 03:05:35)
Compiler: PyPy 7.3.1 with MSC v.1912 32 bit
Executing Module: sample_waiting_prog.py
Total Time of execution = 10.083690881729126 (10.08 Seconds)

Date: Sunday, 16-Aug-2020 09:55:12 PM
Python Version: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
Compiler: Default
Executing Module: sample_waiting_prog.py
Total Time of execution = 10.002431631088257 (10.00 Seconds)
```

##### Output of `sample_data_loading.py` 's Batch File:
```
Date: Sunday, 16-Aug-2020 10:04:38 PM
Python Version: 3.6.9 (2ad108f17bdb, Apr 07 2020, 03:05:35)
Compiler: PyPy 7.3.1 with MSC v.1912 32 bit
Executing Module: sample_data_loading.py
Total Time of execution = 4.749809980392456 (4.75 Seconds)

Date: Sunday, 16-Aug-2020 10:04:40 PM
Python Version: 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
Compiler: Default
Executing Module: sample_data_loading.py
Total Time of execution = 1.1019093990325928 (1.10 Seconds)
```

### Conclusion
As observed in the above output, the PyPy compiler's execution speed is more or less equal to the native Python as of date 16-Aug-2020, may be due to the PyPy standalone binary is only available of Python 3.6 32-bit for Windows till date, or may be due to virtual environment compatibility of all new PyPy. Either ways, the development on this is rapid and soon it is expected to beat CPython in speed, and the usage of cross-compilers/implementations like Cython, Jython, IronPython, CLPython, PyObjC, Ruby Python, etc. are replaced by Python's compiler PyPy alone.

<h1 class="footer">This page will be posted time-to-time. Happy Pythoning!!</h1>
