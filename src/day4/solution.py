class BingoData():
    def __init__(self, file):
        self.lines = [line.strip() for line in open(file, "r").readlines()]


    def get_numbers_to_draw(self):
        return [int(i) for i in self.lines[0].split(",")]

    def get_rows(self):
        boards_data = self.lines[2:]
        rows = [row.replace("  ", " ").split(" ") for row in boards_data if row != ""]
        for x in range(len(rows)):
            for y in range(len(rows[x])):
                rows[x][y] = int(rows[x][y])

        return rows


class BingoCard():
    def __init__(self, rows):
        self.card = rows


    def get_card(self):
        return self.card

    def cross_number(self, number):
        for x in range(len(self.card)):
            for y in range(len(self.card)):
                if self.card[x][y] == number:
                    self.card[x][y] = -1

    def check_win(self):
        for i in range(len(self.card)):
            if sum(self.card[i]) == -5:
                return True

        column_sums = [sum(i) for i in zip(*self.card)]
        if -5 in column_sums:
            return True

        return False


    def get_score(self, lastNumber):
        score = 0
        for x in range(len(self.card)):
            for y in range(len(self.card)):
                if self.card[x][y] != -1:
                    score += self.card[x][y]

        return score * lastNumber


def get_winning_board_score(cards, numbers_to_draw):
    for number in numbers_to_draw:
        for card in cards:
            card.cross_number(number)
            if card.check_win():
                return card.get_score(number)

def get_losing_board_score(cards, numbers_to_draw):
    scores = []
    for number in numbers_to_draw:
        for card in cards:
            card.cross_number(number)
            if card.check_win():
                scores.append(card.get_score(number))
                cards = [card for card in cards if not card.check_win()]

    return scores[-1]


if __name__ == "__main__":
    bingodata = BingoData("input.txt")
    rows = bingodata.get_rows()
    card_len = 5
    bingo_cards = [BingoCard(rows[i*card_len : i*card_len+card_len]) for i in range(len(rows) // card_len)]

    winning_score = get_winning_board_score(bingo_cards, bingodata.get_numbers_to_draw())
    losing_score = get_losing_board_score(bingo_cards, bingodata.get_numbers_to_draw())

    print(f"Part 1: {winning_score}")
    print(f"Part 2: {losing_score}")
