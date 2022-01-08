import itertools
import numpy as np

class TransParentOrigami():
    def __init__(self, file):
        with open(file, "r") as f:
            data = f.read()
        dots_data = data.split("\n\n")[0]
        folds_data = data.split("\n\n")[1]
        self.dots = []
        self.folds = []
        for dots in dots_data.split("\n"):
            x, y = dots.split(",")[0], dots.split(",")[1]
            self.dots.append([int(x), int(y)])
        for folds in folds_data.split("\n"):
            direction, value = folds.split("=")[0][-1], folds.split("=")[1]
            self.folds.append({"direction": direction, "value": int(value)})

    def fold(self, times):
        for i in range(times):
            direction, value = self.folds[i]["direction"], self.folds[i]["value"]
            for dot in self.dots:
                if direction == "x" and dot[0] > value:
                    dot[0] = value - (dot[0] - value)
                elif direction == "y" and dot[1] > value:
                    dot[1] = value - (dot[1] - value)
            self.remove_duplicates()

    def fold_all(self):
        self.fold(len(self.folds))

    def draw(self):
        all_x, all_y = [], []
        for (x, y) in self.dots:
            all_x.append(x)
            all_y.append(y)
        paper = np.zeros((max(all_y) + 1, max(all_x) + 1))

        for (x, y) in self.dots:
            paper[y][x] = 1
        return paper

    def remove_duplicates(self):
        new_dots = sorted(self.dots)
        self.dots = list(new_dots for new_dots, _ in itertools.groupby(new_dots))


if __name__ == "__main__":
    origami1 = TransParentOrigami("input.txt")
    origami1.fold(1)
    print(f"Part 1: {len(origami1.dots)}")

    origami2 = TransParentOrigami("input.txt")
    origami2.fold_all()
    paper = origami2.draw()
    print("Part 2:")
    for y in range(len(paper)):
        part2 = ""
        for x in range(len(paper[0])):
            if paper[y][x] == 1:
                part2 += "#"
            else:
                part2 += "."
        print(part2)
