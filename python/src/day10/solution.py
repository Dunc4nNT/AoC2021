from syntaxes import SYNTAX_PAIRS, SYNTAX_ILLEGAL_SCORES, SYNTAX_EXTRA_SCORES

class SyntaxScoring():
    def __init__(self, file):
        self.data = [line.strip("\r\n") for line in open(file, "r")]
        self.pairs = SYNTAX_PAIRS
        self.illegal_scores = SYNTAX_ILLEGAL_SCORES
        self.extra_scores = SYNTAX_EXTRA_SCORES

    def find_illegal(self, line):
        closings_expected = []
        for char in line:
            if char in self.pairs:
                closings_expected.append(self.pairs[char])
            else:
                expected = closings_expected.pop()
                if char !=  expected:
                    return char

    def find_all_illegals(self):
        all_illegals = []
        for line in self.data:
            illegal = self.find_illegal(line)
            if illegal:
                all_illegals.append(illegal)

        return all_illegals

    def score_illegals(self):
        score = 0
        illegals = self.find_all_illegals()
        for illegal in illegals:
            score += self.illegal_scores[illegal]

        return score

    def find_extras(self):
        extras = []
        for line in self.data:
            if self.find_illegal(line):
                continue

            expected_closings = []
            for char in line:
                if char in self.pairs:
                    expected_closings.insert(0, self.pairs[char])
                else:
                    expected_closings.remove(char)
            extras.append(expected_closings)

        return extras

    def score_extras(self):
        extras = self.find_extras()
        scores = []

        for line in extras:
            line_score = 0
            for char in line:
                line_score = line_score * 5 + self.extra_scores[char]
            scores.append(line_score)
        scores.sort()

        return scores[len(scores)//2]


if __name__ == "__main__":
    syntax = SyntaxScoring("input.txt")

    print(f"Part 1: {syntax.score_illegals()}")
    print(f"Part 2: {syntax.score_extras()}")
