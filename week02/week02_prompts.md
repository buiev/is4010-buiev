# Lab 02: Prompt Engineering Solutions

## Problem 1: Debugging

**My Prompt:**

> You are a senior Python developer reviewing code. I have a function that's supposed to calculate the sum of all **even** numbers in a list, but it's returning incorrect results. Here's the buggy code:
>
> ```python
> def sum_of_evens(numbers):
>     """Calculate the sum of all even numbers in a list.
>
>     Parameters
>     ----------
>     numbers : list of int
>         A list of integers.
>
>     Returns
>     -------
>     int
>         The sum of all even numbers in the list.
>     """
>     total = 0
>     for num in numbers:
>         if num % 2 == 1:  # This line has a bug!
>             total += num
>     return total
> ```
>
> The problem: The condition `num % 2 == 1` checks for **odd** numbers, not even numbers. A number is even when `num % 2 == 0`, and odd when `num % 2 == 1`.
>
> Please identify the logical error and provide the corrected version of this function in a Python code block.

**AI's Corrected Code:**

```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 0:  # Fixed: Check for even numbers (remainder 0)
            total += num
    return total
```

**What I Learned:** The modulo operator `%` returns the remainder of division. For even/odd detection, `num % 2 == 0` means the number is even (no remainder when divided by 2), while `num % 2 == 1` or `num % 2 != 0` means it's odd. The bug was a simple logic error—using the wrong condition operator.

---

## Problem 2: Refactoring

**My Prompt:**

> You are a senior Python developer. I have a function that works correctly but is written in a non-Pythonic way. Please refactor it to be more concise, readable, and idiomatic Python:
>
> ```python
> def get_names_of_adults(users):
>     """Given a list of user dictionaries, returns a list of names of users
>     who are 18 or older.
>
>     Parameters
>     ----------
>     users : list of dict
>         List of user dictionaries with 'name' and 'age' keys.
>
>     Returns
>     -------
>     list of str
>         Names of users who are 18 or older.
>     """
>     results = []
>     for i in range(len(users)):
>         if users[i]['age'] >= 18:
>             results.append(users[i]['name'])
>     return results
> ```
>
> Specifically, I'd like you to:
> 1. Use a more Pythonic iteration pattern (iterate over items, not indices)
> 2. Consider using a list comprehension for a more concise solution
> 3. Improve variable naming if needed
>
> Please provide the refactored code in a Python code block with a brief explanation of the improvements.

**AI's Refactored Code:**

```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    # List comprehension approach (most Pythonic)
    return [user['name'] for user in users if user['age'] >= 18]

    # Alternative: More explicit but still Pythonic
    # adult_names = []
    # for user in users:
    #     if user['age'] >= 18:
    #         adult_names.append(user['name'])
    # return adult_names
```

**What I Learned:** The original code used index-based iteration (`for i in range(len(users))`), which is not idiomatic Python. Pythonic improvements include:
- **Direct iteration**: `for user in users` directly accesses items instead of using indices
- **List comprehension**: `[user['name'] for user in users if user['age'] >= 18]` is more concise and readable
- These patterns are more efficient and more aligned with Python's philosophy of readability

---

## Problem 3: Documenting

**My Prompt:**

> You are a senior Python developer. I have a working function that calculates the area of a rectangle, but it's missing professional documentation. Please write a complete NumPy-style docstring for this function:
>
> ```python
> def calculate_area(length, width):
>     if length <= 0 or width <= 0:
>         raise ValueError("Length and width must be positive numbers.")
>     return length * width
> ```
>
> The docstring should include:
> 1. A brief one-line summary
> 2. A more detailed description (if needed)
> 3. Parameters section with types and descriptions
> 4. Returns section with type and description
> 5. Raises section documenting the ValueError exception
> 6. Examples section with doctest-compatible examples
>
> Please provide the complete function with the NumPy-style docstring in a Python code block.

**AI's Documented Code:**

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Computes the area of a rectangle given its length and width.
    Both dimensions must be positive numbers; otherwise, a ValueError
    is raised.

    Parameters
    ----------
    length : float or int
        The length of the rectangle. Must be a positive number.
    width : float or int
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    float or int
        The area of the rectangle (length × width).

    Raises
    ------
    ValueError
        If length or width is less than or equal to 0.

    Examples
    --------
    >>> calculate_area(5, 4)
    20
    >>> calculate_area(3.5, 2.0)
    7.0
    >>> calculate_area(-5, 4)
    Traceback (most recent call last):
        ...
    ValueError: Length and width must be positive numbers.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**What I Learned:** NumPy-style docstrings are the professional standard for Python documentation. Key components include:
- **Summary**: A one-line description of what the function does
- **Description**: Optional, provides more context
- **Parameters**: Documents each parameter with type and purpose
- **Returns**: Describes the return value's type and meaning
- **Raises**: Documents any exceptions the function might raise
- **Examples**: Includes executable doctest examples showing typical usage and edge cases
- This standard format is used in scientific Python libraries and makes code self-documenting

---

## Reflection

Through this lab, I learned:

1. **Debugging with AI**: Effective debugging prompts should explain what the code should do, what it's actually doing wrong, and ask for specific corrections.

2. **Refactoring with AI**: AI can help identify non-idiomatic code patterns and suggest Pythonic alternatives. List comprehensions, proper iteration patterns, and clear variable names make code more readable.

3. **Documenting with AI**: Professional NumPy-style docstrings follow a consistent structure that makes code self-documenting. Including parameter types, return values, exceptions, and examples is essential for maintainable code.

4. **CPTF Framework Power**: Providing Context, Persona, Task, and Format in prompts significantly improves AI responses compared to vague requests. The more specific the prompt, the better the output.

    Raises
    ------
    ValueError
        If length or width are not positive numbers.
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width