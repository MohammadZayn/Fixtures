import pytest

@pytest.fixture(scope="session")
def fixture_sess(request):
    yield
    print("session printed")

@pytest.fixture(scope="class")
def fixture_clss(request):
    yield
    print("class printed")

@pytest.fixture(scope="module")
def fixture_modl(request):
    yield
    print("module printed")

@pytest.fixture(scope="function")
def fixture_func(request):
    yield
    print("function printed")

@pytest.mark.usefixtures("fixture_sess", "fixture_clss","fixture_modl","fixture_func")
class TestClass:
    def testone(self):
        print('Successfully implemented')