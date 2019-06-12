from modules.merge import merge
from modules.split_list import split_list



def merge_sort(l: list, func: callable) -> list:
  """
  consumes a list and a sorting function that returns a boolean
  sorts elements using a merge sort algorythm
  returns the sorted array

  >>> merge_sort([3, 5, 2, 7, 1, 6, 4], (lambda x y: x > y)) -> [1, 2, 3, 4, 5, 6, 7]
  >>> merge_sort(["z", "A", "w", "b", "N", "X", "d"], (lambda x y: x > y)) -> 
        ["A", "N", "X", "b", "d", "w", "z"]
  """
  if type(l) != list or not callable(func):
    raise TypeError('function: merge_sort must be passed types (list, callable)')

  if len(l) > 1:
    [left, right] = split_list(l)
    leftSorted = merge_sort(left, func)
    rightSorted = merge_sort(right, func)

    return merge(leftSorted, rightSorted, func)
  
  return l