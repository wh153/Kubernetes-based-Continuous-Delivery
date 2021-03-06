from main import add
from main import exponent
from main import factorial
from main import fib


'''
assert == add(3,4), "add"
assert 25 == exponent(5,2)
assert 120 == factorial(5)
assert 13 == fib(7)
assert 144 == fib(12)
'''  
    

def test_add():
    assert {"total":7} == add(3,4)
    
def test_exponent():
    assert {"result":25} == exponent(5,2)

def test_factorial():
    assert {"result":120} == factorial(5)

def test_fib():
    assert {"result":13} == fib(7)
    assert {"result":144} == fib(12)