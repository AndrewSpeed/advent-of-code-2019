from part_1.solution import program_output


def test_program_works_for_simple_addition():
    program_input = "1,0,0,0,99"
    expected_program_output = "2,0,0,0,99"

    assert program_output(program_input) == expected_program_output


def test_program_works_for_simple_multiplication():
    program_input = "2,3,0,3,99"
    expected_program_output = "2,3,0,6,99"

    assert program_output(program_input) == expected_program_output


def test_program_works_for_complex_multiplication():
    program_input = "2,4,4,5,99,0"
    expected_program_output = "2,4,4,5,99,9801"

    assert program_output(program_input) == expected_program_output


def test_program_works_for_addition_and_multiplication():
    program_input = "1,1,1,4,99,5,6,0,99"
    expected_program_output = "30,1,1,4,2,5,6,0,99"

    assert program_output(program_input) == expected_program_output
