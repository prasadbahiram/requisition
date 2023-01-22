
import pytest


#@pytest.mark.skip
@pytest.mark.xfail
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because string do not match"

@pytest.mark.smoke
def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"

@pytest.fixture()
def setup():
    print("I will be executing first")

def test_fixtureDemo(setup):
    print("I will be execute steps in fixtureDemo method")
