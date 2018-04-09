def push(stack, top, item):
    """Pushes item to top of stack"""
    stack[top] = item


def pop(stack, top):
    """Returns topmost item of stack"""
    # Return False if stack is empty
    if top == 0:
        return False
    item = stack[top - 1]
    stack[top - 1] = None
    return item
