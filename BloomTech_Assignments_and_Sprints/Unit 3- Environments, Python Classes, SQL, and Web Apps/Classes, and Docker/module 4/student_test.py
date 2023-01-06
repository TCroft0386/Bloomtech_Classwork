import pytest
from student import student_generator
import student
from student import BloomtechStudent


@pytest.fixture
def my_student1():
    '''creates student'''
    return student()
    
def passing_test():
    assert BloomtechStudent.AmIpassing(70) == 'Passing'

def individual_test():
    assert type(BloomtechStudent.individual('Logan',23,36,85)) ==  str
    
def grade_test(num):
    assert BloomtechStudent.gradeaftertest(num) < 1
    


grade_test(52)
