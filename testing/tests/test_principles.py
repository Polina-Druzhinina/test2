import sys
sys.path.append("../src")
#TODO make it with `pip install -e .`
from math_demo import (
    add,
    add_with_bug
)

def test_addition():
    assert add(2, 2) == 4, "Function did not return 4"
    print("Test BASIC ADDITION")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4, "Function did not return 4"
    assert add_with_bug(0, 0) == 0
    print("Test BASIC ADDITION PASSED (does it mean code ok?)")
    #assert add_with_bug(6, 7) == 13 #will fail here

#дублирование логики
def test_addition_dublicated():
    assert add(2,3) == 2+3 #предполагается что этот плюс не используется в той функции

def test_addition_overcomplicated():
    #formal valid test but too slow
    for  i in range(0, 2**32):
        for j in range(0, 2**32): 
            assert add(i,j) == sum([i, j])  #не должны использовать все наборы входных параметров
            assert add(-i, -j) == sum([-i,-j])
            assert add(-i, j) == sum([-i,j])
            assert add(i, -j) == sum([i,-j])
if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_dublicated()
    #test_addition_overcomplicated() 