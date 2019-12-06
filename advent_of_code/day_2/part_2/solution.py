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


def item_for(instruction_pointer, program):
    return program[program[instruction_pointer]]


def add(instruction_pointer, program):
    storage_instruction_pointer = program[instruction_pointer + 3]

    item_1 = item_for(instruction_pointer + 1)
    item_2 = item_for(instruction_pointer + 2)

    program[storage_instruction_pointer] = item_1 + item_2
    return instruction_pointer + 4, program


def multiply(instruction_pointer, program):
    storage_instruction_pointer = program[instruction_pointer + 3]

    item_1 = item_for(instruction_pointer + 1)
    item_2 = item_for(instruction_pointer + 2)

    program[storage_instruction_pointer] = item_1 * item_2
    return instruction_pointer + 4, program


def program_output(program_input):
    instruction_pointer = 0
    continue_execution = True
    program = list(map(int, program_input.split(",")))

    while instruction_pointer < len(program) and continue_execution:
        opcode = OpCode(program[instruction_pointer])

        if opcode == OpCode.HALT_EXECUTION:
            continue_execution = False
        elif opcode == OpCode.ADD:
            instruction_pointer, program = add(instruction_pointer, program)
        else:
            instruction_pointer, program = multiply(instruction_pointer, program)

    return ",".join(list(map(str, program)))


if __name__ == "__main__":
    input_file_path = (Path(__file__).parent / RELATIVE_INPUT_FILE_PATH).resolve()
    program_input = file_contents(input_file_path)
    print(f"Program output: {program_output(program_input)}")
