import pytest
import main as m

SORTED_LIST = [1, 2, 3, 4, 5]
SEMI_RANDOM_LIST = [2, 4, 3, 5, 1]
def main():
    test_list_creation()
    test_check_sorted()
    test_bubble_sort()
    
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
    list = m.List(length=len(SEMI_RANDOM_LIST), algorithm="bogo", start_list=SEMI_RANDOM_LIST)
    for i in range(len(SEMI_RANDOM_LIST)):
        assert list.pillars[i].value == SEMI_RANDOM_LIST[i]
        
    list = m.List(algorithm="bogo", start_list=SEMI_RANDOM_LIST)
    assert list.algorithm == "bogo"

def test_check_sorted():
    # test ckheck sorted function
    list = m.List(length=len(SORTED_LIST), algorithm="bogo", start_list=SORTED_LIST)
    assert list.check_sorted() == True
    
    list = m.List(length=len(SEMI_RANDOM_LIST), algorithm="bogo", start_list=SEMI_RANDOM_LIST)
    assert list.check_sorted() == False
    
def test_bubble_sort():
    list = m.List(length=len(SEMI_RANDOM_LIST), algorithm="bubble", start_list=SEMI_RANDOM_LIST)
    list.sort()
    print(list)
    assert list.check_sorted() == True
    
if __name__ == "__main__":
    main()