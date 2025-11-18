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
        ("@abc", "@A."),
        ("@843A", "@8."),
        ("--**abc", "--**A."),
    ],
)
def test_given_value_for_initial(input_text, initials):
    result = Initial().operate(input_text)
    assert result == initials

def test_initials_remove_extra_whitespace():
    input_text = "     Eastern    Michigan   University "
    expected = "E. M. U."
    assert Initial().operate(input_text) == expected
