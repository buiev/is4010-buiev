# Lab 04: Data Structures & AI

## Problem 1: Finding Common Items

**My Prompt:**
> I have two very large lists of product IDs. I need to find the items that appear in both lists. The order doesn't matter and I want it to be very fast. Which Python data structure should I use and why?

**AI Recommendation:**
> **Recommendation:** Python `set`
> **Reasoning:** Sets are optimized for fast membership testing. Using the `.intersection()` method or the `&` operator on two sets is significantly faster (O(min(len(s), len(t)))) than iterating through lists (O(n*m)), and sets automatically handle uniqueness.

## Problem 2: User Profile Lookup

**My Prompt:**
> I have a list of user dictionaries. I frequently need to look up a specific user's details by their username. Performance is critical. What data structure should I use to store this data for fast lookups?

**AI Recommendation:**
> **Recommendation:** Python `dictionary`
> **Reasoning:** Dictionaries act as a hash map, allowing for O(1) (constant time) average lookup speeds. Storing users with the username as the key allows for instant retrieval, whereas searching a list requires iterating through every element (O(n)).

## Problem 3: Listing Even Numbers

**My Prompt:**
> I have a list of sensor readings (integers). I need to filter out the odd numbers and keep only the even ones. The order must stay exactly the same as the original list. What is the best Pythonic way to do this?

**AI Recommendation:**
> **Recommendation:** Python `list` (via List Comprehension)
> **Reasoning:** Lists maintain insertion order, which is a requirement here. A list comprehension `[x for x in data if x % 2 == 0]` is efficient and Pythonic, creating a new list with only the desired elements while preserving their original sequence.