import pytest

#all the py file name should either start or end with the name 'test'
#even the METHODS inside the pytest file should start with the name 'test' as mentioned below

def test_m1():
    a = 3
    b = 4
    assert a+1 == b, "test failed"
    assert a == b, "test failed as a and b are not same"

def test_m2():
    name = 'selenium'
    assert name.upper() == "SELENIUM"

def test_m3():
    assert True

def test_m4():
    assert False



