def merge(a: list, b: list, func: callable) -> list:
  """
  Takes in two sorted lists
  Joins them one element at a time 
  Selecting bassed on the passed sorting function
  Returns a newlist

  >>> merge([1, 2], [3, 4], (lambda x, y: x < y)) -> [1, 2, 3, 4]
  >>> merge([1, 2], [3], (lambda x, y: x < y))    -> [1, 2, 3]
  """
  if type(a) != list or type(b) != list or not callable(func):
    raise TypeError('function: merge(a, b, func) must be passed types (list, list, callable)')

  if b == None: return a
  result = []
  while len(a) > 0 and len(b) > 0:
    if func(a[0], b[0]):
      result.append(a[0])
      a.remove(a[0])
    else:
      result.append(b[0])
      b.remove(b[0])

  # add any remaining items to the list
  result += a
  result += b
  
  return result