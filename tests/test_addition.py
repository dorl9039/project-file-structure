# import calculator_app.addition
from calculator_app import addition


def test_addition():
    # Assert
    assert addition.perform_operation(1, 1) == 2
    assert addition.perform_operation(800, 88) == 888
    assert addition.perform_operation(-1, 1) == 0
    assert addition.perform_operation(addition.perform_operation(2, 2), 4) == 8