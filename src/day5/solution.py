class Data():
    def __init__(self):
        self.max_x = 0
        self.max_y = 0

    def get_coordinates(self, file):
        coordinates = []
        with open(file, "r") as data:
            for line in data:
                x1, y1, x2, y2 = line.replace(" -> ", ",").replace("\n", "").split(",")
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                if x1 > self.max_x:
                    self.max_x = x1
                elif x2 > self.max_x:
                    self.max_x = x2
                elif y1 > self.max_y:
                    self.max_y = y1
                elif y2 > self.max_y:
                    self.max_y = y2
                coordinates.append((x1, y1, x2, y2))

        return coordinates

    def create_diagram(self):
        return [[0 for x in range(self.max_x+1)] for y in range(self.max_y+1)]

    def fill_coordinates(self, diagram, x1, y1, x2, y2):
        while x1 != x2 or y1 != y2:
            diagram[y1][x1] += 1
            if x1 > x2:
                x1 -= 1
            elif x1 < x2:
                x1 += 1
            if y1 > y2:
                y1 -= 1
            elif y1 < y2:
                y1 += 1
        diagram[y2][x2] += 1
        return

    def fill_pt1(self, diagram, coordinates):
        for coor in coordinates:
            if coor[0] == coor[2] or coor[1] == coor[3]:
                self.fill_coordinates(diagram, coor[0], coor[1], coor[2], coor[3])
        return diagram

    def fill_pt2(self, diagram, coordinates):
        for coor in coordinates:
            self.fill_coordinates(diagram, coor[0], coor[1], coor[2], coor[3])
        return diagram

    def count_overlap(self, diagram):
        counter = 0
        for y in range(len(diagram)):
            for x in range(len(diagram[0])):
                if diagram[y][x] >= 2:
                    counter += 1
        return counter


if __name__ == "__main__":
    data = Data()
    coordinates = data.get_coordinates("input.txt")
    diagram = data.create_diagram()
    data.fill_pt1(diagram, coordinates)
    part1_amount = data.count_overlap(diagram)

    diagram = data.create_diagram()
    data.fill_pt2(diagram, coordinates)
    part2_amount = data.count_overlap(diagram)

    print(f"Part 1: {part1_amount}")
    print(f"Part 2: {part2_amount}")
