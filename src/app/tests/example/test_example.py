import pytest
#https://pypi.org/project/pytest-mock/

@pytest.mark.parametrize(
        "input_data, expected_data",
        [
            (123, "abc"),
            (12, "abc"),
            (13, "abc"),
            (12345, "abc"),
            (12398, "abc"),
            pytest.param(12300, "abc", id="belelekelel"),
        ]


)
def test_parametrize(input_data, expected_data):
    print(f"input: {input_data}, expected: {expected_data}")

def test_fixture(example_fixture):
    print(example_fixture)