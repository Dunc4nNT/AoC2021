from itertools import permutations


digits = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


class SevenSegmentDisplay():
    def __init__(self, file):
        self.data = []
        self.data_after = []
        with open(file, "r") as data:
            self.data = data.readlines()
        for line in self.data:
            self.data_after.append(line.strip("\r\n").split(" | ")[1])

    def count_easy_digits(self):
        counter = 0
        for data in self.data_after:
            parts = data.split(" ")
            for part in parts:
                if len(part) in [2, 3, 4, 7]:
                    counter += 1

        return counter

    def count_all_digits(self):
        total = 0

        for line in self.data:
            data_before, data_after = line.split(" | ")
            data_before = data_before.split()
            data_after = data_after.split()

            for perm in permutations("abcdefg"):
                to = str.maketrans("abcdefg", "".join(perm))
                data_before_ = ["".join(sorted(code.translate(to))) for code in data_before]
                data_after_ = ["".join(sorted(code.translate(to))) for code in data_after]
                if all(code in digits for code in data_before_):
                    total += int("".join(str(digits[code]) for code in data_after_))
                    break

        return total


if __name__ == "__main__":
    display = SevenSegmentDisplay("input.txt")

    print(f"Part 1: {display.count_easy_digits()}")
    print(f"Part 2: {display.count_all_digits()}")
