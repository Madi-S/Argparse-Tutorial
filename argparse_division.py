# Here we learn about:
# 1) Positional (mandatory) arguments, which do not include '-'
# 2) Some advanced parameters for creating an argument


import argparse

parser = argparse.ArgumentParser(description='Argparse tutorial')

argument_display_name = 'nums'
help_info_display = 'Pass two numbers for division'

parser.add_argument(argument_display_name,
                    help=help_info_display, type=int, nargs=2)
                    
# nargs - takes '+' for 1 or more arguments or a specified number of arguments needed (int)
# type - (str be the default) specify the type of argument  needed
# help - information that displays when --help or -h is called
# first two parameters - short and long names for parameters (like div and division), but positional arguments take only one name without '-'

args = parser.parse_args()

if args.nums:
    # args.nums is a list, so we can access numbers by indexes
    print(args.nums[0] // args.nums[1])
    
    
    
'''
Example of usage:

1.
λ python argparse_division.py 5 2
2


2.
λ python argparse_division.py 5 2 3
usage: argparse_division.py [-h] nums nums
argparse_division.py: error: unrecognized arguments: 3


3.
λ python argparse_division.py
usage: argparse_division.py [-h] nums nums
argparse_division.py: error: the following arguments are required: nums


4.
λ python argparse_division.py one two
usage: argparse_division.py [-h] nums nums
argparse_division.py: error: argument nums: invalid int value: 'one'
'''
