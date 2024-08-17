import pytest

# This code will help you run the test cases in the order way
class Test_Cases:

    @pytest.mark.run(order=1)
    def test_MethodA(self):
        print("Running Method A...")

    @pytest.mark.run(order=5)
    def test_MethodE(self):
        print("Running Method E...")

    @pytest.mark.run(order=4)
    def test_MethodD(self):
        print("Running Method D...")

    @pytest.mark.run(order=3)
    def test_MethodC(self):
        print("Running Method C...")

    @pytest.mark.run(order=2)
    def test_MethodB(self):
        print("Running Method B...")