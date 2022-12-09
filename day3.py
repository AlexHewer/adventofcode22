'''Advent of Code - Rucksack'''

def return_value(c: str) -> int: #A=27
    '''calculate the value of each letter'''
    if ord(c) < 91:
        return ord(c) - 38
    else:
        return ord(c) - 96

def part_one(file: list[str]):
    '''part one of the challenge'''
    total: int = 0

    for line in file:
        length = len(line)
        comp1 = line[0:int(length/2)]
        comp2 = line[int(length/2):length]
        dup_letter: str
        for letter in comp1:
            if letter in comp2:
                dup_letter = letter
        total += return_value(dup_letter)

    print(f"The total is {total}")

def part_two(file: list[str]):
    '''part two of the challenge'''
    count: int = 0
    total: int = 0
    group: list[str] = []
    for line in file:
        group.append(line.strip())
        count += 1
        if count == 3:
            common = set.intersection(*map(set,group))
            total += return_value(common.pop())
            group.clear()
            count = 0
    print(f"The total is {total}")



f = open("day3.txt", "r", encoding="utf-8")
lines: list[str] = f.readlines()
f.close()

part_one(lines)
part_two(lines)
