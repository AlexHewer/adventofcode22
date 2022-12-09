'''Advent of Code Day 1 - Highest calorie elf'''

f = open("day1.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

calories = []
temp: int = 0

for line in lines:
    if line != "\n":
        temp += int(line)
    else:
        calories.append(temp)
        temp = 0

calories.sort(reverse=True)
print(f"The top elf is carrying {calories[0]} calories")
print(f"The top three elves are carrying {calories[0] + calories[1] + calories[2]} calories")
