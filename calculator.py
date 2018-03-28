import sys
import argparse
from object_oriented.stack import Stack

parser = argparse.ArgumentParser()
parser.add_argument(
    '--imperative',
    '-i',
    help='Use imperative implementation of stack',
    action='store_true')
args = parser.parse_args(sys.argv[1:])

expression = input("Enter postfix expression: ").split()

if not args.imperative:
    pass
else:
    pass
