import pytest


@pytest.mark.xfail
def test_persondeatils():
    print("I'm going to print the details of the most awaited person")
    test_details()


def test_details():
    list = 'My name is mohammad',"im a good boy but not a bad as you"
    print(list)
    test_ageheight()

@pytest.mark.skip
def test_ageheight():
    h = "6 feet"
    age = 24
    print(f"My height is {h} and My age is {age}")
