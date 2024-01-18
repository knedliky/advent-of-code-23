with open('./data.txt', 'r') as f:
    strings = f.read().splitlines()

(_, games) = strings.split(':')

# Part one
def part_one(red:int, green:int, blue:int) -> int:
    for game in strings: 
        counter = 0
        for round in game.split(';'):


# Part two
def part_two():
    pass

print("The answer to part one is: ", part_one(strings))