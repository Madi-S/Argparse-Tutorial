# Here we learn about:
# 1) Combining positional and optional arguments
# 2) How to set the default value for the argument
# 3) Make user choose the value for the argument from the given list

import argparse
import math
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


parser = argparse.ArgumentParser(description='Argparse tutorial')

# When the only parameter from the given list is needed for the argument:
parser.add_argument(
    '-m', '--math', help='Show mathematical constants', choices=['e', 'pi'])

# Choices takes a list with values that can be specified
# If the user specifies the value that does not exist in the choices list, the program will throw an error

# When argument can be modified (set default for non-given arguments):
parser.add_argument('-e', '--exc_path', help='Specify executable path for the ChromeDriver',
                    default=r'C:\Users\khova\Desktop\Python\chromedriver.exe')

# Specify the default value in default that can be modified or left like that

args = parser.parse_args()

if args.math == 'e':
    print(math.e)
elif args.math == 'pi':
    print(math.pi)

try:
    driver = webdriver.Chrome(args.exc_path)
    driver.get('https://github.com/Madi-S/Argparse-Tutorial')
    sleep(5)
    driver.quit()
except WebDriverException:
    print('Specify the correct executable path or not specify it at all')

    
'''
Example of usage:

1.
λ python argparse_advanced.py -m e
2.718281828459045


2.
λ python argparse_advanced.py --math pi
3.141592653589793


3.
λ python argparse_advanced.py -m pi e
usage: argparse_tutorial.py [-h] [-m {e,pi}] [-e EXC_PATH]
argparse_tutorial.py: error: unrecognized arguments: e


4.
λ python argparse_advanced.py -m abc
usage: argparse_tutorial.py [-h] [-m {e,pi}] [-e EXC_PATH]
argparse_tutorial.py: error: argument -m/--math: invalid choice: 'abc' (choose from 'e', 'pi')


5.
λ python argparse_tutorial.py --math e -e C:\\Users\\khova\\Desktop\\Python\\chromedriver.exe
2.718281828459045

DevTools listening on ws://127.0.0.1:59316/devtools/browser/cfd980da-eec7-4a69-8017-dbbdfb0a9b62
[11740:11536:1030/195559.199:ERROR:device_event_log_impl.cc(208)] [19:55:59.199] Bluetooth: bluetooth_adapter_winrt.cc:1076 Getting Default Adapter failed.


6.
λ python argparse_tutorial.py --exc_path C:\\Users\\khova\\Desktop\\NotPython\\chromedriver.exe
Specify the correct executable path or not specify it at all
'''
