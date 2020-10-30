# Here we learn about:
# 1) Optional arguments (non-mandatory), which do include '-'
# 2) Some other advanced parameters for creating an argument
# 3) Short and long names for paramers


import argparse
import sys



short_name = '-v'
long_name = '--version'


parser.add_argument(short_name, long_name,
                    help='Show your current python version', action='store_true')

parser.add_argument('-d', '--directory',
                    help='Show your current python directory', action='store_true')

# action = 'store_true' means nothing needs to be specified in the console, e.g.:
# first two parameters for positional arguments are for short and long names of the argument (starting with '-' and '--' respectively)
# python argparse_info.py --version

args = parser.parse_args()

if args.version:  # if '-v' or '--version' was written args.version becomes True, None by default
    print(sys.version)

if args.directory:
    print(sys.executable)
