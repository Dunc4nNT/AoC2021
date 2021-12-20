def get_adjacent(data, x, y):
    values = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
    return [(x1, y1) for (x1, y1) in values if 0 <= x1 < len(data[0]) and 0 <= y1 < len(data)]

def is_low_point(data, adjacent_cells, x, y):
    if data[y][x] == 9:
        return False
    for (x2, y2) in adjacent_cells:
        if data[y2][x2] < data[y][x]:
            return False
    return True

def find_low_points(data):
    low_points = []
    for y in range(len(data)):
        for x in range(len(data[0])):
            adjacent_cells = get_adjacent(data, x, y)
            if is_low_point(data, adjacent_cells, x, y):
                low_points.append((x, y))

    return low_points

def get_low_points_sum(low_points):
    total = 0
    for (x, y) in low_points:
        total += data[y][x] + 1
    return total

def get_basin(data, x, y):
    basin = []
    visited = []

    cells_to_check = [(x, y)]
    while cells_to_check:
        (x1, y1) = cells_to_check.pop()
        if (x1, y1) not in visited:
            visited.append((x1, y1))

            if data[y1][x1] != 9:
                basin.append((x1, y1))
                adjacent_cells = get_adjacent(data, x1, y1)
                for (x2, y2) in adjacent_cells:
                    if (x2, y2) not in visited:
                        cells_to_check.append((x2, y2))

    return basin

def get_all_basins(data):
    basins = []
    low_points = find_low_points(data)
    for (x, y) in low_points:
        basins.append(get_basin(data, x, y))
    return basins


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        given_input = f.readlines()
    data = []
    for line in given_input:
        data.append([int(i) for i in line if i.isdigit()])

    low_points = find_low_points(data)

    print(f"Part 1: {get_low_points_sum(low_points)}")


    basins = get_all_basins(data)
    basin_lens = [len(x) for x in basins]
    biggest_basins = []
    for i in range(3):
        biggest_basins.append(max(basin_lens))
        basin_lens.remove(max(basin_lens))
    size = biggest_basins[0]
    for i in biggest_basins[1:]:
        size *= i

    print(f"Part 2: {size}")
