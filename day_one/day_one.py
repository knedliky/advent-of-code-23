def part_one(data: str) -> int:
    number = ""
    for i in data:
        if i.isdigit():
            number += i
            break

    for i in data[::-1]:
        if i.isdigit():
            number += i
            break

    return 0 if number == "" else int(number)


def part_two(data: str) -> int:
    number = ""
    data_copy = data
    digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for digit in digits:
        if digit in data:
            data_copy = (
                data_copy[: data.find(digit)]
                + str(digits.index(digit) + 1)
                + data_copy[data.find(digit) + 1 :]
            )
            data_copy = (
                data_copy[: data.rfind(digit)]
                + str(digits.index(digit) + 1)
                + data_copy[data.rfind(digit) + 1 :]
            )

    for i in data_copy:
        if i.isdigit():
            number += i
            break

    for i in data_copy[::-1]:
        if i.isdigit():
            number += i
            break

    return 0 if number == "" else int(number)


with open("./data.txt", "r") as f:
    strings = f.read().splitlines()

print("Answer to part one: ", np.sum([part_one(string) for string in strings]))
print("Answer to part two: ", np.sum([part_two(string) for string in strings]))
