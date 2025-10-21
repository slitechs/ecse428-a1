import cdc

calculator = cdc.Calculator()

#T_PUSH_REAL1
def test_push_pop_real():
    arg = "push 5 pop"
    assert calculator.execute(arg) == "5 + j0"

# T_PUSH_CPLX1
def test_push_pop_complex_compact():
    arg = "push -2.5-j0.25 pop"
    assert calculator.execute(arg) == "-2.5 - j0.25"

# T_PUSH_CPLX2
def test_push_pop_complex_spaced():
    arg = "push 3 + j 4 pop"
    assert calculator.execute(arg) == "3 + j4"
