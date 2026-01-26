# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**
> Context: I have a Python function that is supposed to sum all even numbers in a list, but it contains a logical error.
> Persona: You are a senior Python developer.
> Task: Identify the bug in the code below and provide the corrected version.
> Format: Provide the corrected code in a Python code block and briefly explain the fix.
>
> Code:
> def sum_of_evens(numbers):
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:  # This line has a bug!
>             total += num
>     return total

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list."""
    total = 0
    for num in numbers:
        # Fixed the condition to check for even numbers (remainder 0)
        if num % 2 == 0:
            total += num
    return total

    def get_names_of_adults(users):
    """Return a list of names of users who are 18 or older."""
    # Used list comprehension for more concise and Pythonic code
    return [user['name'] for user in users if user['age'] >= 18]

    def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters
    ----------
    length : float
        The length of the rectangle.
    width : float
        The width of the rectangle.

    Returns
    -------
    float
        The calculated area (length * width).

    Raises
    ------
    ValueError
        If length or width are not positive numbers.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width