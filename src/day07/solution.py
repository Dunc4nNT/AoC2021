import sys

class CrabFuel():
    def __init__(self, file):
        self.crabs = [int(crab) for crab in open(file, "r").readline().split(",")]

    def cheapest_cost(self):
        cheapest_cost = sys.maxsize
        min_value = min(self.crabs)
        max_value = max(self.crabs)

        for i in range(min_value, max_value):
            cost = 0
            for crab in self.crabs:
                cost += abs(crab - i)
            if cost < cheapest_cost:
                cheapest_cost = cost

        return cheapest_cost

    def cheapest_cost_nth_triangle(self):
        cheapest_cost = sys.maxsize
        min_value = min(self.crabs)
        max_value = max(self.crabs)

        for i in range(min_value, max_value):
            cost = 0
            for crab in self.crabs:
                n = abs(crab - i)
                cost += int(n * (n + 1) / 2)
            if cost < cheapest_cost:
                cheapest_cost = cost

        return cheapest_cost


if __name__ == "__main__":
    crab_fuel = CrabFuel("input.txt")

    print(f"Part 1: {crab_fuel.cheapest_cost()}")
    print(f"Part 2: {crab_fuel.cheapest_cost_nth_triangle()}")
