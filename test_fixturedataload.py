import pytest


@pytest.mark.usefixtures("dataload")
class Testdata:

    def test_autocap(self, dataload): 
        print(dataload[0])
        print(dataload[1])