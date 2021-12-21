class DumboOctopus():
    def __init__(self, file):
        with open(file, "r") as f:
            given_input = f.readlines()
        self.data = []
        for line in given_input:
            self.data.append([int(i) for i in line if i.isdigit()])

    def get_adjacent(self, x, y):
        values = [(x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)]
        return [(x1, y1) for (x1, y1) in values if 0 <= x1 < len(self.data[0]) and 0 <= y1 < len(self.data)]

    def simulate_days(self, n):
        total_flashes = 0

        for _ in range(n):
            flashes = self.simulate_day()
            total_flashes += flashes

        return total_flashes

    def get_bright_day(self):
        total_octopuses = len(self.data) * len(self.data[0])
        day = 0
        while not self.check_bright_day(total_octopuses):
            day += 1
        return day + 1

    def check_bright_day(self, octopuses):
        return self.simulate_day() == octopuses

    def simulate_day(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                self.data[y][x] += 1
        return self.check_flashed([])

    def check_flashed(self, flashed):
        flash_counter = 0
        cells_to_check = []

        for y in range(len(self.data)):
            for x in range(len(self.data[0])):
                if self.data[y][x] > 9 and (x, y) not in flashed:
                    self.data[y][x] = 0
                    cells_to_check.append((x, y))
                    flashed.append((x, y))
                    flash_counter += 1

        if cells_to_check:
            for (x, y) in cells_to_check:
                for (x1, y1) in self.get_adjacent(x, y):
                    if (x1, y1) not in flashed:
                        self.data[y1][x1] += 1
            return flash_counter + self.check_flashed(flashed)
        else:
            return flash_counter

if __name__ == "__main__":
    simulationpt1 = DumboOctopus("input.txt")
    print(f"Part 1: {simulationpt1.simulate_days(100)}")

    simulationpt2 = DumboOctopus("input.txt")
    print(f"Part 2: {simulationpt2.get_bright_day()}")
