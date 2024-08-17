# Any py test file start or ends with test_xxxx name otherwise it will not consider
# method name or function name should start with test word.
import pytest


def test_demigods():
    print('Good Morning Mohammad Zyan')
    msg = "hi"
    assert msg == "hi","NOt matched the msg please check and try again"
    print('demi god is present in the list')
    list = ["sara", "zayn", "malik"]
    assert "zayn" in list, "Not present pleas e check the other list and try again"
    for x in list:
        print(x) 


def test_demigoddess():
    print("Im gonna print the demi goddess list")
    test_demigods()

@pytest.mark.smoke
def test_ageheight():
    h = "6 feet"
    age = 24
    print(f"My height is {h} and My age is {age}")
