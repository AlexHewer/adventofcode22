'''Advent of Code - Rock Paper Scissors'''

def rps_calculate(in_value: str) -> int:
    '''Return the amount of points per round'''
    match in_value:
        case "A X": return 4
        case "B X": return 1
        case "C X": return 7
        case "A Y": return 8
        case "B Y": return 5
        case "C Y": return 2
        case "A Z": return 3
        case "B Z": return 9
        case "C Z": return 6
    return 0

def rps_calculate2(in_value: str) -> int:
    '''Return the amount of points per round'''
    match in_value:
        case "A X": return 3
        case "B X": return 1
        case "C X": return 2
        case "A Y": return 4
        case "B Y": return 5
        case "C Y": return 6
        case "A Z": return 8
        case "B Z": return 9
        case "C Z": return 7
    return 0


f = open("day2.txt", "r", encoding="utf-8")
lines: list[str] = f.readlines()
f.close()

points: int = 0
points2: int = 0

for line in lines:
    points += rps_calculate(line[0:3])
    points2 += rps_calculate2(line[0:3])

print(f"You total {points} points")
print(f"You then total {points2} points")
    