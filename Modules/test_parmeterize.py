import pytest

class TestParam:

    @pytest.mark.parametrize("num1,num2",[(1,1),(4,6),(7,7),(8.10,8.10)])
    def test_EqualOrNot(self,num1,num2):
        print(' I am gonna comparison work')
        assert num1 == num2, "This case numbers are not equal to both"