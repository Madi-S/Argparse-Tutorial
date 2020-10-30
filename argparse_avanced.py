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

# When only parameter from given list is needed for the argument:
parser.add_argument(
    '-m', '--math', help='Show mathematical constants', choices=['e', 'pi'])

# Choices takes list with values that can be specified
# If user specifies the value that does not exists in the choices list, the program will throw an error

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
