import pytest
import cdc

calculator = cdc.Calculator()

#T_PUSH_REAL1
def test_push_pop_real():
    arg = "push 5 pop"
    assert(calculator.calculate(arg) == "5 + j0")
