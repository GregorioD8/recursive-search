def recursive_search(arr, target, index=0):
    # Base case: if index reaches the length of the array, target is not found
    if index == len(arr):
        return False
    # Check if the current element is the target
    if arr[index] == target:
        return True
    # Recursively search the next element
    return recursive_search(arr, target, index + 1)

# Test cases
print(recursive_search([1, 2, 3], 2))  # Output: True
print(recursive_search([3, 2, 1], 4))  # Output: False