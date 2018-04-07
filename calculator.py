import sys
import argparse
from object_oriented.stack import Stack


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


parser = argparse.ArgumentParser()
parser.add_argument(
    '--imperative',
    '-i',
    help='Use imperative implementation of stack',
    action='store_true')
args = parser.parse_args(sys.argv[1:])

expression = input("Enter postfix expression: ").split()

if not args.imperative:
    stack = Stack()
    for i in range(len(expression)):
        try:
            if is_number(expression[i]):
                stack.push(expression[i])
            elif expression[i] in ['+', '-', '*', '/', '%', '**']:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.push(str(eval(op1 + expression[i] + op2)))
            else:
                sys.exit('Unrecognized operation')
        except TypeError as e:
            sys.exit('Invalid postfix expression')
    print(stack.pop())
else:
    pass
