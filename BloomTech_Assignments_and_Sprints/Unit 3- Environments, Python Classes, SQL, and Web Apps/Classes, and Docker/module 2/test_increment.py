from increment import increment

def test_increment():
    '''test for increment'''
    assert increment(4) == 5, 'increment not working'  
    assert increment(4) == 5, 'increment not working'
    assert increment(3) == 4, 'increment not working'

