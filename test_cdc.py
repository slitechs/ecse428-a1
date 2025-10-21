import cdc

calculator = cdc.Calculator()

# T_PUSH_REAL1
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

# T_POP_ERR1
def test_pop_error_underflow():
    arg = "pop"
    assert calculator.execute(arg) == "Error: stack underflow"

# T_ADD_REAL1
def test_add_real():
    arg = "push 2 push 5 add pop"
    assert calculator.execute(arg) == "7 + j0"

# T_ADD_CPLX1
def test_add_complex():
    arg = "push 3+j4 push 1-j2 add pop"
    assert calculator.execute(arg) == "4 + j2"

# T_ADD_ERR1
def test_add_error_underflow():
    arg = "push 3 add"
    assert calculator.execute(arg) == "Error: stack underflow"

# T_SUB_REAL1
def test_sub_real():
    arg = "push 5 push 2 sub pop"
    assert calculator.execute(arg) == "3 + j0"

# T_SUB_CPLX1
def test_sub_complex():
    arg = "push 3+j4 push 1-j2 sub pop"
    assert calculator.execute(arg) == "2 + j6"

# T_SUB_ERR1
def test_sub_error_underflow():
    arg = "sub"
    assert calculator.execute(arg) == "Error: stack underflow"

# T_MUL_REAL1
def test_mul_real():
    arg = "push 3 push -2 mul pop"
    assert calculator.execute(arg) == "-6 + j0"

# T_MUL_CPLX1
def test_mul_complex():
    arg = "push 1+j2 push 3-j4 mul pop"
    assert calculator.execute(arg) == "11 + j2"

# T_MUL_ERR1
def test_mul_error_underflow():
    arg = "mul"
    assert calculator.execute(arg) == "Error: stack underflow"

# T_DIV_REAL1
def test_div_real():
    arg = "push 8 push 2 div pop"
    assert calculator.execute(arg) == "4 + j0"

# T_DIV_CPLX1
def test_div_complex():
    arg = "push 4+j2 push 1+j1 div pop"
    assert calculator.execute(arg) == "3 - j1"

# T_DIV_ERR1
def test_div_error_divide_by_zero_real():
    arg = "push 1 push 0 div"
    assert calculator.execute(arg) == "Error: division by zero"

# T_DIV_ERR2
def test_div_error_divide_by_zero_complex():
    arg = "push 1+j0 push 0+j0 div"
    assert calculator.execute(arg) == "Error: division by zero"

# T_DEL_REAL1
def test_delete_real():
    arg = "push 1 push 2 delete pop"
    assert calculator.execute(arg) == "1 + j0"

# T_DEL_CPLX1
def test_delete_complex():
    arg = "push 1+j1 push 2+j3 delete pop"
    assert calculator.execute(arg) == "1 + j1"

# T_DEL_ERR1
def test_delete_error_underflow():
    arg = "delete"
    assert calculator.execute(arg) == "Error: stack underflow"

# T_ABS_REAL1
def test_abs_real():
    arg = "push 3 ABS pop"
    assert calculator.execute(arg) == "3 + j0"

# T_ABS_CPLX1
def test_abs_complex():
    arg = "push 3+j4 ABS pop"
    assert calculator.execute(arg) == "5 + j0"

# T_ABS_ERR1
def test_abs_error_underflow():
    arg = "ABS"
    assert calculator.execute(arg) == "Error: stack underflow"

# T_SIN_REAL1
def test_sin_real():
    arg = "push 0 SIN pop"
    assert calculator.execute(arg) == "0 + j0"

# T_SIN_CPLX1
def test_sin_complex():
    arg = "push 1+j1 SIN pop"
    assert calculator.execute(arg) == "1.298457581 + j0.634963915"

# T_SIN_ERR1
def test_sin_error_underflow():
    arg = "SIN"
    assert calculator.execute(arg) == "Error: stack underflow"

# T_ASIN_REAL1
def test_asin_real():
    arg = "push 0 ASIN pop"
    assert calculator.execute(arg) == "0 + j0"

# T_ASIN_CPLX1
def test_asin_complex():
    arg = "push 1+j1 ASIN pop"
    assert calculator.execute(arg) == "0.666239432 + j1.061275061"

# T_ASIN_ERR1
def test_asin_error_underflow():
    arg = "ASIN"
    assert calculator.execute(arg) == "Error: stack underflow"

# T_COS_REAL1
def test_cos_real():
    arg = "push 0 COS pop"
    assert calculator.execute(arg) == "1 + j0"

# T_COS_CPLX1
def test_cos_complex():
    arg = "push 1+j1 COS pop"
    assert calculator.execute(arg) == "0.833730025 - j0.988897706"

# T_COS_ERR1
def test_cos_error_underflow():
    arg = "COS"
    assert calculator.execute(arg) == "Error: stack underflow"

# T_ACOS_REAL1
def test_acos_real():
    arg = "push 1 ACOS pop"
    assert calculator.execute(arg) == "0 + j0"

# T_ACOS_CPLX1
def test_acos_complex():
    arg = "push 1+j1 ACOS pop"
    assert calculator.execute(arg) == "0.904556894 - j1.061275061"

# T_ACOS_ERR1
def test_acos_error_underflow():
    arg = "ACOS"
    assert calculator.execute(arg) == "Error: stack underflow"

# T_SQR_REAL1
def test_sqr_real():
    arg = "push 5 SQR pop"
    assert calculator.execute(arg) == "25 + j0"

# T_SQR_CPLX1
def test_sqr_complex():
    arg = "push 1+j2 SQR pop"
    assert calculator.execute(arg) == "-3 + j4"

# T_SQR_ERR1
def test_sqr_error_underflow():
    arg = "SQR"
    assert calculator.execute(arg) == "Error: stack underflow"

# T_SQRT_REAL1
def test_sqrt_real():
    arg = "push 4 SQRT pop"
    assert calculator.execute(arg) == "2 + j0"

# T_SQRT_CPLX1
def test_sqrt_complex():
    arg = "push -1 SQRT pop"
    assert calculator.execute(arg) == "0 + j1"

# T_SQRT_ERR1
def test_sqrt_error_underflow():
    arg = "SQRT"
    assert calculator.execute(arg) == "Error: stack underflow"
