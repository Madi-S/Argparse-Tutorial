#

import argparse
import sys



short_name = '-v'
long_name = '--version'


parser.add_argument(short_name, long_name,
                    help='Show your current python version', action='store_true')
parser.add_argument('-d', '--directory',
                    help='Show your current python directory', action='store_true')

args = parser.parse_args()

if args.version:
    print(sys.version)

if args.directory:
    print(sys.executable)
