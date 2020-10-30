import argparse
import math
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

# First two examples cover 90% of needs, however, sometimes some advanced techincs must be used:
#


parser = argparse.ArgumentParser(description='Argparse tutorial')

# When only parameter from given list is needed for the argument:
parser.add_argument(
    '-m', '--math', help='Show mathematical constants', choices=['e', 'pi'])

# When argument can be modified (set default for non-given arguments):
parser.add_argument('-e', '--exc_path', help='Specify executable path for the ChromeDriver',
                    default=r'C:\Users\khova\Desktop\Python\chromedriver.exe')


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
