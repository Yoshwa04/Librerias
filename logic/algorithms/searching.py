from typing import List, TypeVar

T = TypeVar('T')  # Generic type that can be compared

def binary_search(arr: List[T], target: T) -> int:
    """
    Devuelve el índice del target en arr si se encuentra, -1 si no está.
    """
    arr.sort()
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
