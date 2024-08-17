import pytest

class TestClass:

    @pytest.mark.integration
    def test_loginbyemail(self):
        print('this is login by email...')
        assert True == True

    @pytest.mark.integration
    def test_loginbyfacebook(self):
        print('this is login by facebook...')
        assert True == True

    @pytest.mark.regression     # Add the these two marker into the ini file
    @pytest.mark.integration
    def test_loginbytwitter(self):
        print('this is login by twitter...')
        assert True == True

    @pytest.mark.regression
    @pytest.mark.integration
    def test_signupbyemail(self):
        print('this is signup by email...')
        assert True == True

    @pytest.mark.regression
    def test_signupbyfacebook(self):
        print('this is signup by facebook...')
        assert True == True

    @pytest.mark.regression
    def test_signupbytwitter(self):
        print('this is signup by twitter...')
        assert True == True