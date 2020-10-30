# Here we learn about:
# 1) Positional (mandatory) arguments, which do no include '-'
# 2) Some advanced parameters for creating an argument


import argparse

parser = argparse.ArgumentParser(description='Argparse tutorial')

argument_display_name = 'nums'
help_info_display = 'Pass two numbers for division'

parser.add_argument(argument_display_name,
                    help=help_info_display, type=int, nargs=2)
                    
# nargs - takes '+' for 1 or more arguments, or specified number of arguments needed (int)
# type - (str be default) specify the type of argument  needed
# help - information that displays when --help or -h is called
# first two parameters - short and long names for parameters (like div and division), but positional arguments take only one name without '-'

args = parser.parse_args()

if args.nums:
    # args.nums is a list, so we can acess numbers by indexes
    print(args.nums[0] // args.nums[1])
