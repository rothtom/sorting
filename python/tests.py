import pytest
import main as m

SORTED_LIST = [1, 2, 3, 4, 5]
SEMI_RANDOM_TUPLE = tuple([2, 4, 3, 5, 1])
    
def test_list_creation():
    # test list creation with a list of length 1 
    list = m.List(length=1, seed=1, algorithm="bogo")
    assert list.algorithm == "bogo"
    assert list.pillars[0].value == 1
    
    #test list algorythm type
    list = m.List(length=1, seed=1, algorithm="bogo")
    assert list.algorithm == "bogo"
    list = m.List(length=1, seed=1, algorithm="bogo-sort")
    assert list.algorithm == "bogo"
    
    # test list creation with fixed list:
    list = m.List(length=len(SEMI_RANDOM_TUPLE), algorithm="bogo", start_tuple=SEMI_RANDOM_TUPLE)
    for i in range(len(SEMI_RANDOM_TUPLE)):
        assert list.pillars[i].value == SEMI_RANDOM_TUPLE[i]
        
    list = m.List(algorithm="bogo", start_tuple=SEMI_RANDOM_TUPLE)
    assert list.algorithm == "bogo"

def test_check_sorted():
    # test ckheck sorted function
    list = m.List(algorithm="bogo", start_tuple=tuple(SORTED_LIST))
    assert list.check_sorted() == True
    
    list = m.List(algorithm="bogo", start_tuple=SEMI_RANDOM_TUPLE)
    assert list.check_sorted() == False
    
def test_bubble_sort():
    list = m.List(algorithm="bubble", start_tuple=SEMI_RANDOM_TUPLE)
    list.sort()
    assert list.check_sorted() == True

def test_bogo_sort():
    list = m.List(algorithm="bogo", start_tuple=tuple([2, 1, 3]))
    list.sort()
    assert list.check_sorted() == True
    
def test_selection_sort():
    list = m.List(algorithm="selection", start_tuple=SEMI_RANDOM_TUPLE)
    list.sort()
    assert list.check_sorted() == True