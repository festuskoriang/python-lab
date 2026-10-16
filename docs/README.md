# Project organization

Separating code into src, tests, and docs is good practice even for a small
project because each folder has a clear purpose: src holds the application
code, tests holds checks that help catch bugs, and docs explains how the
project works. This organization makes files easier to find, change, and
maintain as the project grows.

# Python imports

In main.py, this import statement connects the program to the functions
defined in utils.py:

```python
from utils import celsius_to_fahrenheit, is_even, square
```

When main.py is run as a script, Python searches the script's directory for a
module named utils and finds utils.py. Python loads that module, making the
named functions available to main.py. The program can then call those
functions to calculate and display results.