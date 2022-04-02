from typing import List


class Connect4:

    def __init__(self, m: int = 6, n: int = 7):
        self.board = self.__create_board(m, n)
        self.is_first_player = True

    @staticmethod
    def __create_board(m: int, n: int) -> List[List[str]]:
        if not (m > 3 and n > 4):
            raise Exception

        board = [['#'] * m for _ in range(n)]

        return board

    def check_board_status(self):
        pass

    def print_board(self):
        m, n = len(self.board), len(self.board[0])
        for i in range(m-1, -1, -1):
            row = ''
            for j in range(n):
                row += self.board[j][i]
            print(row)

    def start(self):
        self.move_randomly()

    def move_randomly(self):
        pass

    def move_with_intelligence(self):
        pass

    def min_max(self):
        pass


class HeuristicStrategy:

    def __init__(self):
        pass
