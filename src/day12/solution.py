from collections import defaultdict, Counter
from time import perf_counter as perf

class PassagePathing():
    def __init__(self, file):
        self.caves = defaultdict(list)
        for line in open(file, "r").readlines():
            line = line.strip("\r\n").split("-")
            self.caves[line[0]].append(line[1])
            self.caves[line[1]].append(line[0])

    def find_paths(self, double_visits, start_node = "start", path = []):
        paths = []
        path = path + [start_node]

        if start_node == "end":
            return [path]

        for node in self.caves[start_node]:
            if node == "start":
                continue

            if node.isupper():
                new_paths = self.find_paths(double_visits, node, path)
                for new_path in new_paths:
                    paths.append(new_path)
            elif double_visits and path.count(node) < 2 and path.count("end") <= 1:
                lower_nodes = [n for n in path if n.islower()]
                if Counter(lower_nodes).most_common(1)[0][1] < 2:
                    new_paths = self.find_paths(double_visits, node, path)
                    for new_path in new_paths:
                        paths.append(new_path)
                elif Counter(lower_nodes).most_common(2)[1][1] < 2:
                    new_paths = self.find_paths(double_visits, node, path)
                    for new_path in new_paths:
                        paths.append(new_path)
            elif node not in path:
                new_paths = self.find_paths(double_visits, node, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths


if __name__ == "__main__":
    pathing = PassagePathing("input.txt")

    print(f"Part 1: {len(pathing.find_paths(False))}")
    print(f"Part 2: {len(pathing.find_paths(True))}")
