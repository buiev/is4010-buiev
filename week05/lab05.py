"""
Lab 05: Functions and Error Handling
Refactored user data processing with robust error handling.
"""

users = [
    {"name": "alice", "age": 30, "is_active": True, "email": "alice@example.com"},
    {"name": "bob", "age": 25, "is_active": False},
    {"name": "charlie", "age": 35, "is_active": True, "email": "charlie@example.com"},
    {"name": "david", "age": "unknown", "is_active": False}
]


def calculate_average_age(users):
    """
    Calculate the average age of users with valid integer ages.
    
    Parameters
    ----------
    users : list
        A list of user dictionaries containing 'age' keys.
    
    Returns
    -------
    float
        The average age of users with valid integer ages, or 0.0 if no valid ages.
    
    Raises
    ------
    None
        Handles errors gracefully by returning 0.0 for edge cases.
    """
    try:
        total_age = 0
        user_count_for_age = 0
        
        for user in users:
            if isinstance(user.get("age"), int):
                total_age += user["age"]
                user_count_for_age += 1
        
        if user_count_for_age == 0:
            print("error: cannot calculate average age of an empty list.")
            return 0.0
        
        return total_age / user_count_for_age
    except (ZeroDivisionError, TypeError) as e:
        print(f"error: failed to calculate average age: {e}")
        return 0.0


def get_active_user_emails(users):
    """
    Get a list of emails from all active users.
    
    Parameters
    ----------
    users : list
        A list of user dictionaries containing 'is_active' and 'email' keys.
    
    Returns
    -------
    list
        A list of email addresses from active users, or empty list if none found.
    
    Raises
    ------
    None
        Handles errors gracefully by returning an empty list for edge cases.
    """
    try:
        active_user_emails = []
        
        for user in users:
            if user.get("is_active") and user.get("email"):
                active_user_emails.append(user["email"])
        
        return active_user_emails
    except (KeyError, AttributeError, TypeError) as e:
        print(f"error: failed to retrieve active user emails: {e}")
        return []


if __name__ == '__main__':
    # Call functions and print results
    avg_age = calculate_average_age(users)
    print(f"average user age: {avg_age:.2f}")

    active_emails = get_active_user_emails(users)
    print(f"active user emails: {active_emails}")
