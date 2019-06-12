import pytest
from split_list import split_list

def test_split_list():
  assert split_list([1, 2, 3, 4]) == [[1, 2], [3, 4]]
  assert split_list([1, 2, 3]) == [[1, 2], [3]]
  
def test_raises_error_string():
  with pytest.raises(TypeError):
    split_list('hello')

def test_raises_error_dict():
  with pytest.raises(TypeError):
    split_list({"message": 'hello'})

def test_raises_error_num():
  with pytest.raises(TypeError):
    split_list(123)
    split_list(2.45)