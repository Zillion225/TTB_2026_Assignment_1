"""
This script finds the common elements between two lists.
"""
from typing import List

def find_common_elements(list1: List[int], list2: List[int]) -> List[int]:
    """
    Finds the common elements between two lists.

    Args:
        list1: The first list of integers.
        list2: The second list of integers.

    Returns:
        A list of common integers.
    """
    return list(set(list1) & set(list2))

def main():
    """
    Main function to demonstrate find_common_elements.
    """
    list_a = [1, 2, 3, 5, 6, 8, 9]
    list_b = [3, 2, 1, 5, 6, 0]
    result_list = find_common_elements(list_a, list_b)
    print(f"Common elements: {result_list}")

if __name__ == "__main__":
    main()
