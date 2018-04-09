# Array-based stack implementation

## Usage

### Creating the stack

```python
max_size = 100  # Can be any integer value
stack = [None] * max_size  # Creates a list of None values
top = 0  # Points to the top of stack
```

### Pushing to the stack

```python
x = 0
push(stack, top, x)
top += 1
```

**Note:** An `IndexError` will be raised after attempting to push to a full stack

### Popping from the stack

```python
x = pop(stack, top)
if x is not None:  # Did not pop from an empty stack
    top -= 1
```

**Note:** Popping from an empty stack returns `None`