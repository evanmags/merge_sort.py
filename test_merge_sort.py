import pytest
from merge_sort import merge_sort

# sorting function for tests
def is_smaller(a, b):
  a = a.split('.')
  b = b.split('.')

  for i in range(3):
    if not len(a) > i: return True
    if not len(b) > i: return False

    if int(a[i]) < int(b[i]): return True
    if int(b[i]) < int(a[i]): return False

def is_less_than(x, y):
  return x < y

def test_merge_sort():
  assert merge_sort(["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"], is_smaller) == ["0.1","1.1.1","1.2","1.2.1","1.11","2","2.0","2.0.0"]
  assert merge_sort(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"], is_smaller) == ["1.0","1.0.2","1.0.12","1.1.2","1.3.3"]
  assert merge_sort(["1.1.2"], is_smaller) == ["1.1.2"]
  assert merge_sort([3, 5, 2, 7, 1, 6, 4], is_less_than) == [1, 2, 3, 4, 5, 6, 7]
  assert merge_sort(["z", "A", "w", "b", "N", "X", "d"], is_less_than) == ["A", "N", "X", "b", "d", "w", "z"]

def test_error_no_func():
  with pytest.raises(TypeError):
    merge_sort([3, 5, 2, 7, 1, 6, 4])
    merge_sort(["z", "A", "w", "b", "N", "X", "d"])

def test_error_no_list():
  with pytest.raises(TypeError):
    merge_sort(is_less_than)

def test_error_passed_string():
  with pytest.raises(TypeError):
    merge_sort("not a list", is_less_than)
    merge_sort([3, 5, 2, 7, 1, 6, 4], "not a function")

def test_error_passed_number():
  with pytest.raises(TypeError):
    merge_sort(133, is_less_than)
    merge_sort([3, 5, 2, 7, 1, 6, 4], 123)
    merge_sort(1.33, is_less_than)
    merge_sort([3, 5, 2, 7, 1, 6, 4], 12.3)

def test_error_passed_dict():
  with pytest.raises(TypeError):
    merge_sort({"dict": "message"}, is_less_than)
    merge_sort([3, 5, 2, 7, 1, 6, 4], {"dict": "message"})
