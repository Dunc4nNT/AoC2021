from collections import Counter

class ExtendedPolymerization():
    def __init__(self, file):
        with open(file, "r") as f:
            lines = f.read()

        # create a counter with all the start value pairs
        # this way i can simply update a counter number, rather than a huge string that gets infinitely big :)
        pairs_data = list(lines.split("\n\n")[0])
        pairs = []
        for i in range(len(pairs_data) - 1):
            pairs.append(pairs_data[i] + pairs_data[i+1])
        self.counter = Counter(pairs)

        # create a dict with all the "rules" about pairs in them
        # also create a base dictionary where all rules have a count of 0
        # used in every step of get_result
        rules_data = lines.split("\n\n")[1].split("\n")
        self.rules = {}
        for rule in rules_data:
            self.rules.update({rule[0] + rule[1]: [rule[0] + rule[-1], rule[-1] + rule[1]]})
        self.rules_base_counter = {rule : 0 for rule in self.rules}

    def get_result(self, steps):
        for _ in range(steps):
            current_counter = self.rules_base_counter.copy()
            for k, v in self.counter.items():
                # increases the values of the new pairs that get created as a result of the old pairs
                # much, much more efficient than going through every single pair on by one :)
                current_counter[self.rules[k][0]] += v
                current_counter[self.rules[k][1]] += v
            self.counter = current_counter

        # count the amount every letter exists in the final "string"
        totals = {}
        for l1, l2 in list(self.counter):
            totals.update({l1 : 0})
            totals.update({l2 : 0})
        for k, v in self.counter.items():
            totals[k[0]] += v
        totals[list(self.counter.keys())[-1][1]] += 1   # because the very last value of the "string" is otherwise missed out

        # delete all keys that have a value of 0
        # this way the Counter returning most common doesn't have a bunch of 0 values in the end
        # which would make it hard to find the least common letter
        keys_to_delete = [key for key, value in totals.items() if value == 0]
        for key in keys_to_delete:
            del totals[key]

        count = Counter(totals).most_common()
        least_common = count[-1]
        most_common = count[0]
        diff = most_common[1] - least_common[1]

        return diff


if __name__ == "__main__":
    print(f"Part 1: {ExtendedPolymerization('input.txt').get_result(10)}")
    print(f"Part 2: {ExtendedPolymerization('input.txt').get_result(40)}")
