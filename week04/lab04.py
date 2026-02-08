def find_common_elements(list1, list2):
    """Find the common elements between two lists.

    Parameters
    ----------
    list1 : list
        The first list of elements.
    list2 : list
        The second list of elements.

    Returns
    -------
    list
        A list of elements common to both list1 and list2.
    """
    # Convert lists to sets to use efficient intersection logic
    set1 = set(list1)
    set2 = set(list2)
    
    # Find the intersection (items in both)
    common_set = set1.intersection(set2)
    
    # Convert back to a list to match the return type requirement
    return list(common_set)

def find_user_by_name(users, name):
    """Find a user's profile by name from a list of user data.

    Parameters
    ----------
    users : list of dict
        A list of dictionaries, where each dictionary represents a user
        and has 'name', 'age', and 'email' keys.
    name : str
        The name of the user to find.

    Returns
    -------
    dict or None
        The dictionary of the found user, or None if no user is found.
    """
    # Iterate through the list to find the matching name.
    for user in users:
        if user["name"] == name:
            return user
    return None

def get_list_of_even_numbers(numbers):
    """Return a new list containing only the even numbers from the input list.

    The order of the numbers in the output list must be the same as the
    order of the even numbers in the input list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    list of int
        A new list containing only the even integers from the input list.
    """
    # Use a list comprehension to filter even numbers while preserving order
    return [num for num in numbers if num % 2 == 0]