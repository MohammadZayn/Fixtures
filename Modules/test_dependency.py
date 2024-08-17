import pytest


class TestCases:
    @pytest.mark.dependency()  # add dependency word to the ini file to avoid errors
    def test_openApp(self):
        assert True

    @pytest.mark.dependency(depends=['TestCases::test_openApp'])  # if app is opened the proceed the below the method
    def test_login(self):
        assert False

    @pytest.mark.dependency(depends=['TestCases::test_login'])
    def test_search(self):
        assert True

    @pytest.mark.dependency(depends=['TestCases::test_login', 'TestCases::test_search'])
    def test_advance_search(self):
        assert True

    @pytest.mark.dependency(depends=['TestCases::test_login'])
    def test_logout(self):
        assert True
