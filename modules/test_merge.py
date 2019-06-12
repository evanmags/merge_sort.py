import pytest
from merge import merge

func = (lambda x, y: x < y)

def test_merge():
  assert merge([1, 2], [3, 4], func) == [1, 2, 3, 4]
  assert merge([1, 2], [3], func) == [1, 2, 3]

def test_error_no_function():
  with pytest.raises(TypeError):
    merge([1, 2], [3])

def test_error_missing_list():
  with pytest.raises(TypeError):
    merge([1, 2], func)

def test_error_passed_string():
  with pytest.raises(TypeError):
    merge([1, 2], "hello", func)

def test_error_passed_number():
  with pytest.raises(TypeError):
    #int
    merge([1, 2], 0, func)
    merge(1, 0, func)
    # float
    merge([1, 2], 12.22,func)
    merge(12.22, 12.22,func)

def test_error_passed_dict():
  with pytest.raises(TypeError):
    merge([1, 2], {"dict": 'dict'}, func)
    merge({"dict": 'dict'}, {"dict": 'dict'}, func)