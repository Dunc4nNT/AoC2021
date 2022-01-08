class SmokeBasin():
    def __init__(self, file):
        with open(file, "r") as f:
            given_input = f.readlines()
        self.data = []
        for line in given_input:
            self.data.append([int(i) for i in line if i.isdigit()])

    def get_adjacent(self, x, y):
        values = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        return [(x1, y1) for (x1, y1) in values if 0 <= x1 < len(self.data[0]) and 0 <= y1 < len(self.data)]

    def is_low_point(self, adjacent_cells, x, y):
        if self.data[y][x] == 9:
            return False
        for (x2, y2) in adjacent_cells:
            if self.data[y2][x2] < self.data[y][x]:
                return False
        return True

    def find_low_points(self):
        low_points = []
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                adjacent_cells = self.get_adjacent(x, y)
                if self.is_low_point(adjacent_cells, x, y):
                    low_points.append((x, y))
        return low_points

    def get_low_points_sum(self):
        total = 0
        for (x, y) in self.find_low_points():
            total += self.data[y][x] + 1
        return total

    def get_basin(self, x, y):
        basin = []
        visited = []

        cells_to_check = [(x, y)]
        while cells_to_check:
            (x1, y1) = cells_to_check.pop()
            if (x1, y1) not in visited:
                visited.append((x1, y1))

                if self.data[y1][x1] == 9:
                    continue
                basin.append((x1, y1))
                adjacent_cells = self.get_adjacent(x1, y1)
                for (x2, y2) in adjacent_cells:
                    if (x2, y2) not in visited:
                        cells_to_check.append((x2, y2))
        return basin

    def get_all_basins(self):
        basins = []
        low_points = self.find_low_points()
        for (x, y) in low_points:
            basins.append(self.get_basin(x, y))
        return basins

    def get_biggest_basins_sum(self):
        basins = self.get_all_basins()
        basin_lens = [len(x) for x in basins]
        biggest_basins = []

        for i in range(3):
            biggest_basins.append(max(basin_lens))
            basin_lens.remove(max(basin_lens))

        size = biggest_basins[0]
        for i in biggest_basins[1:]:
            size *= i
        return size


if __name__ == "__main__":
    smokebasin = SmokeBasin("input.txt")
    print(f"Part 1: {smokebasin.get_low_points_sum()}")
    print(f"Part 2: {smokebasin.get_biggest_basins_sum()}")
