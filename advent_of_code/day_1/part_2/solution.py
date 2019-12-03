from pathlib import Path

RELATIVE_INPUT_FILE_PATH = "data/input.txt"


def file_contents(file_path):
    with open(file_path, "r+") as file:
        for line in file:
            yield line


def fuel_for_mass(mass):
    return int(mass / 3) - 2


def fuel_for_mass_and_fuel(mass):
    fuel_required = 0
    fuel = fuel_for_mass(mass)

    while fuel > 0:
        fuel_required += fuel
        fuel = fuel_for_mass(fuel)

    return fuel_required


def fuel_required_for_modules(modules_file_path):
    fuel_required = 0

    for module_mass in file_contents(modules_file_path):
        fuel_required += fuel_for_mass_and_fuel(int(module_mass))

    return fuel_required


def total_fuel_requirement():
    input_file_path = (Path(__file__).parent / RELATIVE_INPUT_FILE_PATH).resolve()
    return fuel_required_for_modules(input_file_path)


if __name__ == "__main__":
    print(f"Total fuel requirement: {total_fuel_requirement()}")
