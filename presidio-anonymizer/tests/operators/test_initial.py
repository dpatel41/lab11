import pytest
from presidio_anonymizer.operators import Initial


def test_correct_name():
    # The operator should report its name as "initial"
    assert Initial().operator_name() == "initial"


@pytest.mark.parametrize(
    "input_text, initials",
    [
        ("John Smith", "J. S."),
        ("john smith", "J. S."),
    ],
)
def test_given_value_for_initial(input_text, initials):
    result = Initial().operate(input_text)
    assert result == initials
