import pytest


class TestSkip:

    @pytest.mark.skip
    def test_signupbyemail(self,setup):
        print('this is signup by email...')
        assert True == True

    def test_signupbyfacebook(self,setup):
        print('this is signup by facebook...')
        assert True == True

    @pytest.mark.skip
    def test_signupbytwitter(self,setup):
        print('this is signup by twitter...')
        assert True == True

    def test_loginbyemail(self,setup):
        print('this is login by email...')
        assert True == True

    @pytest.mark.skip
    def test_loginbyfacebook(self,setup):
        print('this is login by facebook...')
        assert True == True

    def test_loginbytwitter(self,setup):
        print('this is login by twitter...')
        assert True == True