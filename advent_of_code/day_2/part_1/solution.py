from pathlib import Path
from enum import Enum

RELATIVE_INPUT_FILE_PATH = "data/input.txt"


class OpCode(Enum):
    ADD = 1
    MULTIPLY = 2
    HALT_EXECUTION = 99


def file_contents(file_path):
    with open(file_path, "r+") as file:
        return file.read()


def add(index, program):
    item_1_index = program[index + 1]
    item_2_index = program[index + 2]
    storage_index = program[index + 3]

    item_1 = program[item_1_index]
    item_2 = program[item_2_index]

    program[storage_index] = item_1 + item_2
    return program


def multiply(index, program):
    item_1_index = program[index + 1]
    item_2_index = program[index + 2]
    storage_index = program[index + 3]

    item_1 = program[item_1_index]
    item_2 = program[item_2_index]

    program[storage_index] = item_1 * item_2
    return program


def program_output(program_input):
    index = 0
    continue_execution = True
    program = list(map(int, program_input.split(",")))

    while index < len(program) and continue_execution:
        opcode = OpCode(program[index])

        if opcode == OpCode.HALT_EXECUTION:
            continue_execution = False
        elif opcode == OpCode.ADD:
            program = add(index, program)
        else:
            program = multiply(index, program)

        index += 4

    return ",".join(list(map(str, program)))


if __name__ == "__main__":
    input_file_path = (Path(__file__).parent / RELATIVE_INPUT_FILE_PATH).resolve()
    program_input = file_contents(input_file_path)
    print(f"Program output: {program_output(program_input)}")
