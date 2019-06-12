import math

def split_list(arr: list) -> list:
  """
  Takes in list
  Calculates the index of the middle element
  Takes two slices of origional list
  Returns new list containing the two halves of the original
  
  >>> split_list([1, 2, 3, 4]) -> [[1, 2], [3, 4]]
  >>> split_list([1, 2, 3]) -> [[1, 2], [3]]
  """
  if type(arr) != list: 
    raise TypeError('function: split_list(arr) must be passed a list')

  halfIndex = int(math.ceil(len(arr)/2))
  firstHalf = arr[:halfIndex]
  secondHalf = arr[halfIndex:]
  return [firstHalf, secondHalf]