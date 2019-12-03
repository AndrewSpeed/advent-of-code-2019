from pathlib import Path

RELATIVE_INPUT_FILE_PATH = "data/input.txt"


def file_contents(file_path):
    with open(file_path, "r+") as file:
        for line in file:
            yield line


def fuel_required_for_modules(modules_file_path):
    fuel_required = 0

    for module_mass in file_contents(modules_file_path):
        fuel_required += int(int(module_mass) / 3) - 2

    return fuel_required


def total_fuel_requirement():
    input_file_path = (Path(__file__).parent / RELATIVE_INPUT_FILE_PATH).resolve()
    return fuel_required_for_modules(input_file_path)


if __name__ == "__main__":
    print(f"Total fuel requirement: {total_fuel_requirement()}")
