# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
# Method name should be proper and have sense
# -k stands for specific regular expression name (eg. CreditCard)
# -s stands for logs in output, -v stands for more info like metadata
# You can run specific file with py.test <filename>
# You can mark test with (@pytest.mark.smoke) this and run as (py.test -m smoke -v -s)
# You can skip test with @pytest.mark.skip
# If you know test failed but not to show result in output at that time @pytest.mark.xfail
# fixtures are used as setup and tear down method for test cases
# conftest file to generalise fixtures and make it available to all test cases
# datadriven and parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end
# after all class methods are executed




import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


def test_secondGreetCreditCard():
    print("Good Morning !")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])


