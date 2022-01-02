import pytest
from breeding import *

def test_find_partner():
    # n isnt in breedable
    assert find_partner(2, [1], 100) is None
    
    # best number is itself, skip the first one
    assert find_partner(2, [1,2], 100) == 2
    
    # best number is itself but its product is too big
    assert find_partner(2, [1,2], 3) is None

    # has to breed with 9 cause 3*3 is in breedable
    assert find_partner(3,[3,9],100)==9

def test_propagate():
    # most basic
    y_true = [2,3,4,9]
    primes = [2,3]
    y_pred,propagated = propogate(primes, primes, max_val=2**14)
    assert len(y_true)==len(y_pred)
    assert all([y_true[i]==y_pred[i] for i in range(len(y_true))])

    # has to skip 2*2 cause 4 is already breed
    primes = [2,3]
    active = [2,3,4]
    y_true =[2,3,6,16]
    y_pred,propagated = propogate(active, primes, max_val=2**14)
    assert len(y_true)==len(y_pred)
    assert all([y_true[i]==y_pred[i] for i in range(len(y_true))])
    
    # dont add back in primes if they dont exist
    active = [3,4,6]
    primes = []
    y_pred,propagated = propogate(active, primes, max_val=2**14)
    y_true = [9,16,36]
    assert len(y_true)==len(y_pred)
    assert all([y_true[i]==y_pred[i] for i in range(len(y_true))])
    
    # check empty unbreedable list logic, 5 and 7 shouldnt duplicate
    active = [2,3,5,7]
    primes = []
    y_true = [4,5,7,9]
    y_pred,propagated = propogate(active, primes, max_val=10)
    