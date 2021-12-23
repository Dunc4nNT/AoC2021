import heapq
import numpy as np

class Chiton():
    def __init__(self, file):
        with open(file, "r") as f:
            given_input = f.readlines()
        data = []
        for line in given_input:
            data.append([int(i) for i in line if i.isdigit()])
        self.data = np.array(data)

        self.connections = {}
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                self.connections[(x, y)] = {"risk": self.data[y][x], "connections": []}
                for (x1, y1) in self.get_adjacent(self.data, x, y):
                    self.connections[(x, y)]["connections"].append((x1, y1))

    def get_adjacent(self, data, x, y):
        values = [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]
        return [(x1, y1) for (x1, y1) in values if 0 <= x1 < len(data[0]) and 0 <= y1 < len(data)]

    def get_result(self):
        start_node = (0, 0)
        end_node = (len(self.data[0]) - 1, len(self.data) - 1)
        # queue = [(0, start_node, [])]
        queue = [(0, start_node)]
        seen = set()

        while queue:
            # (risk, node, path) = heapq.heappop(queue)
            (risk, node) = heapq.heappop(queue)
            if node not in seen:
                # path = path + [node]
                seen.add(node)

                if node == end_node:
                    return risk
                for next_node in self.connections[node]["connections"]:
                    next_risk = self.connections[next_node]["risk"]
                    # heapq.heappush(queue, (risk + next_risk, next_node, path))
                    heapq.heappush(queue, (risk + next_risk, next_node))

    def increase_size(self, amount):
        vertical = self.data.copy()
        for i in range(amount-1):
            vertical = np.vstack([self.data, vertical + 1])
        horizontal = vertical.copy()
        for i in range(amount-1):
            horizontal = np.hstack([vertical, horizontal + 1])

        for x in range(len(horizontal[0])):
            for y in range(len(horizontal)):
                if horizontal[y][x] > 9:
                    horizontal[y][x] -= 9

        self.data = horizontal

        self.connections = {}
        for x in range(len(self.data[0])):
            for y in range(len(self.data)):
                self.connections[(x, y)] = {"risk": self.data[y][x], "connections": []}
                for (x1, y1) in self.get_adjacent(self.data, x, y):
                    self.connections[(x, y)]["connections"].append((x1, y1))

if __name__ == "__main__":
    print(f"Part 1: {Chiton('input.txt').get_result()}")

    chiton = Chiton("input.txt")
    chiton.increase_size(5)
    print(f"Part 2: {chiton.get_result()}")
