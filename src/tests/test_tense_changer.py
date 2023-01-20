import pytest
import tense_changer

data_test = (
    (
        "eu am trecut prin fata casei.",
        "eu trecui prin fata casei."
     ),
)

@pytest.mark.parametrize("input, expected", data_test)
def test_main(input, expected):
    actual = tense_changer.main(input)
    assert actual == expected
