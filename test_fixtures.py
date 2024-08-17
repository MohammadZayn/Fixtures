import pytest


@pytest.mark.usefixtures("setup")
class Mak:

    def test_fixture1(self):
        print("I will execute mid operations in the 1st method")

    def test_fixture2(self):
        print("I will execute mid operations in the 2nd method")

    def test_fixture4(self):
        print("I will execute mid operations in the 3rd method")
