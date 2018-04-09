import sys
import argparse
from object_oriented.stack import Stack
from imperative.stack import push, pop


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
    print('Using object-oriented implementation of stack')
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
        # Popped from an empty stack
        except TypeError:
            sys.exit('Invalid postfix expression')
    result = stack.pop()
    # Postfix expression invalid if stack is not empty
    if stack.pop():
        sys.exit('Invalid postfix expression')
    print(result)
else:
    print('Using imperative implementation of stack')
    stackSize = len(expression)
    stack = [None] * stackSize
    top = 0
    for i in range(stackSize):
        try:
            if is_number(expression[i]):
                push(stack, top, expression[i])
                top += 1
            elif expression[i] in ['+', '-', '*', '/', '%', '**']:
                op2 = pop(stack, top)
                if not op2:
                    raise TypeError
                top -= 1
                op1 = pop(stack, top)
                if not op1:
                    raise TypeError
                top -= 1
                push(stack, top, str(eval(op1 + expression[i] + op2)))
                top += 1
            else:
                sys.exit('Unrecognized operation')
        # Popped from an empty stack
        except TypeError:
            sys.exit('Invalid postfix expression')
    result = pop(stack, top)
    top -= 1
    # Postfix expression invalid if stack is not empty
    if top != 0:
        sys.exit('Invalid postfix expression')
    print(result)
