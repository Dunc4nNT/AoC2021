class LanternFish():
    def __init__(self, file):
        self.data = [int(i) for i in open(file, "r").readline().split(",")]

    def simulateFishBirth(self, days):
        amount_of_fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for fish in self.data:
            amount_of_fish[fish] += 1

        for day in range(days):
            fishToSpawn = amount_of_fish[0]

            for i in range(8):
                amount_of_fish[i] = amount_of_fish[i+1]
            amount_of_fish[8] = fishToSpawn
            amount_of_fish[6] += fishToSpawn

        return sum(amount_of_fish)


if __name__ == "__main__":
    fish = LanternFish("input.txt")
    new_fish_amount = fish.simulateFishBirth(80)
    fish_amount_part2 = fish.simulateFishBirth(256)

    print(f"Part 1: {new_fish_amount}")
    print(f"Part 2: {fish_amount_part2}")
