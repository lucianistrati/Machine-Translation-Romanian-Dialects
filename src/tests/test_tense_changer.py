import pytest
from oltenizator import tense_changer

data_test = (
    (
        "eu am trecut prin fata casei.",
        "eu trecui prin fata casei."
     ),
    (
        " Tu ai plecat in parcare.",
        " Tu plecași in parcare."
     ),
    (
        "Eu m-am abătut de la drum.",
        "Eu m-abătui de la drum."
     ),
    (
        "Noi am fost la plimbare.",
        "Noi furăm la plimbare."
     ),
    (
        "Ei au negat minciuna.",
        "Ei negară minciuna."
     ),
    (
        "Au negat minciuna.",
        "negară minciuna."
     ),
    (
        "Eu am argumentat bine.",
        "Eu argumentai bine."
    ),
    (
        "A aranjat camera.",
        "aranjă camera."
    ),
    (
        "Voi ați crezut in mine.",
        "Voi crezurăţi in mine."
    )
)


@pytest.mark.parametrize("input, expected", data_test)
def test_main(input, expected):
    actual = tense_changer.main(input)
    assert actual == expected


data_test_reverse = (
    (
        "eu argumentai mancare.",
        "eu am trecut prin fata casei."
    ),
)
@pytest.mark.parametrize("input, expected", data_test_reverse)
def test_main_reverse(input, expected):
    actual = tense_changer.main(input, True)
    assert actual == expected
