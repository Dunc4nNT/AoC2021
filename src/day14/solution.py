from collections import Counter

class ExtendedPolymerization():
    def __init__(self, file):
        with open(file, "r") as f:
            lines = f.read()
        self.data = list(lines.split("\n\n")[0])
        self.pairs = {}
        pairs_data = lines.split("\n\n")[1].split("\n")
        for pair in pairs_data:
            pair_lst = pair.split(" -> ")
            self.pairs.update({pair_lst[0]: pair_lst[1]})

    def increase_steps(self, n):
        for _ in range(n):
            count = 0
            for i in range(len(self.data) - 1):
                if self.pairs[self.data[count] + self.data[count+1]]:
                    self.data.insert(count+1, self.pairs[self.data[count] + self.data[count+1]])
                    count += 2

if __name__ == "__main__":
    pt1 = ExtendedPolymerization("input.txt")
    pt1.increase_steps(10)
    counts = Counter(pt1.data).most_common()
    least_common = counts[-1]
    most_common = counts[0]

    print(f"Part 1: {most_common[1] - least_common[1]}")

    pt2 = ExtendedPolymerization("input.txt")
    pt2.increase_steps(40)
    counts = Counter(pt2.data).most_common()
    least_common = counts[-1]
    most_common = counts[0]

    print(f"Part 2: {most_common[1] - least_common[0]}")
