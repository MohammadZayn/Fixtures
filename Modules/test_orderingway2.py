import pytest

# This code will help you run the test cases in the order way
# Firstly we have create a pytest.ini file and then have to declare in order format of methods to run
class Test_Cases:

    @pytest.mark.first
    def test_MethodA(self):
        print("Running Method A...")

    @pytest.mark.fifth
    def test_MethodE(self):
        print("Running Method E...")

    @pytest.mark.fourth
    def test_MethodD(self):
        print("Running Method D...")

    @pytest.mark.third
    def test_MethodC(self):
        print("Running Method C...")

    @pytest.mark.second
    def test_MethodB(self):
        print("Running Method B...")