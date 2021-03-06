import pytest

"""
Install pytest
===============
pip install pytest

#all the py file name should either start or end with the name 'test'
#even the METHODS inside the pytest file should start with the name 'test' as mentioned below


#pytest commands to execute the pytest
#do the command execution on the terminal/cmd

py.test --> to execute the pytest testcases
(or)
py.test <testfilename.py> --> to execute the specific pytest testcase

py.test -k login -v  --> this command will execute only the METHOD's who's name is like/similar 'login'

py.test -m login --> to execute only test cases associated with the MARKER login
py.test PytestSessions\test_Pytest_Basics1.py -m login --> specific file from a dir

"""

"""
To execute the testcases in the PARALLEL Mode
==============================================
pip install pytest-xdist

to execute the test cases, as usual, execute the below command
py.test PytestSessions\test_webpage_login.py

to execute the test cases PARALLELLY
py.test PytestSessions\test_webpage_login.py -n 3

"""

"""
To generate pytest html report
===============================
pip install pytest-html

when executing the test cases and generate HTML report, use the below command

py.test <filename.py> -v -s --help=<htmlreportname.html>


"""

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





