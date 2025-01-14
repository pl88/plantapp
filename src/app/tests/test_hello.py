from app.hello import hello

# Next steps
# @pytest.parametrize
# mocker

def test_hello():
    test_name = "Piotr"
    result = hello(test_name)
    expected_result = "Rise and shine Piotr"
    assert result == expected_result
