import Wallet
import pytest


@pytest.fixture
def wallet_20():
    '''Creates a scenario where we have a 
    wallet with $20 in it.'''
    return Wallet(20)


def test_balance():
    '''doc'''
    assert Wallet().balance == 0, 'error message'
    assert Wallet(20).balance == 20


def test_spend_cash(wallet_20):
    '''doc'''
    # wallet_20 = Wallet(20)
    assert wallet_20.balance == 20
    wallet_20.spend_cash(10)
    assert wallet_20.balance == 10
    assert wallet_20.spend_cash(
        10) == '''You can afford it, it cost $10. Current balance is now $0'''


def test_add_cash(wallet_20):
    '''doc'''
    # wallet_20 = Wallet(20)
    wallet_20.add_cash(50)
    assert wallet_20.balance == 70
    assert wallet_20.add_cash(20) == 'Added $20 to the wallet.'