"""Advent Of Code - https://adventofcode.com/2022/day/4"""

def main():
    """This is the main body of logic"""
    lines: list[str] = get_lines()
    overlap_counter: int = 0
    partial_overlap_counter: int = 0
    for line in lines: #15-60,14-59
        assignments: list[str] = line.strip().split(",")
        elf1: list[str] = assignments[0].split("-")
        elf2: list[str] = assignments[1].split("-")

        if ((int(elf1[0]) >= int(elf2[0])) and (int(elf1[1]) <= int(elf2[1])) or
            (int(elf2[0]) >= int(elf1[0])) and (int(elf2[1]) <= int(elf1[1]))):
            overlap_counter += 1

        if ((int(elf1[0]) >= int(elf2[0])) and (int(elf1[0]) <= int(elf2[1])) or
            (int(elf2[0]) >= int(elf1[0])) and (int(elf2[0]) <= int(elf1[1]))):
            partial_overlap_counter += 1

    print(f"The total overlap is {overlap_counter}")
    print(f"The total partial overlap is {partial_overlap_counter}")


def get_lines() -> list[str]:
    """Return a list of each line in the file."""
    file = open("day4.txt", "r", encoding="utf-8")
    lines: list[str] = file.readlines()
    file.close()
    return lines

if __name__ == "__main__":
    main()
