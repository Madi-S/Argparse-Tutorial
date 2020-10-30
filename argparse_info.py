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


'''
Example:

C:\Users\khova\Desktop\Python\Code\GitHub\Argparse Tutorial (master -> origin)
λ python argparse_tutorial.py --help
usage: argparse_info.py [-h] [-v] [-d]

Argparse tutorial

optional arguments:
  -h, --help       show this help message and exit
  -v, --version    Show your current python version
  -d, --directory  Show your current python directory


λ python argparse_info.py -v
3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)]


C:\Users\khova\Desktop\Python\Code\GitHub\Argparse Tutorial (master -> origin)
λ python argparse_tutorial.py --version
3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)]


C:\Users\khova\Desktop\Python\Code\GitHub\Argparse Tutorial (master -> origin)
λ python argparse_info.py --directory
C:\Users\khova\AppData\Local\Programs\Python\Python38-32\python.exe


C:\Users\khova\Desktop\Python\Code\GitHub\Argparse Tutorial (master -> origin)
λ python argparse_info.py --directory -v
3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)]
C:\Users\khova\AppData\Local\Programs\Python\Python38-32\python.exe


'''
