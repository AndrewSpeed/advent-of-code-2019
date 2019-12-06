from pathlib import Path

RELATIVE_INPUT_FILE_PATH = "data/input.txt"


def file_contents(file_path):
    with open(file_path, "r+") as file:
        return file.read()


def solution():
    pass


if __name__ == "__main__":
    print(f"Solution output goes here")
