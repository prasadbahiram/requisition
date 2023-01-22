import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be executing last")


@pytest.fixture()
def dataLoad():
    print("User profile data is being created")
    return ["Rahul", "Shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","Prasad","Bahiram"), ("Firefox","Vaishali"),("IE","Bahiram")])
def crossBrowser(request):
    return request.param
